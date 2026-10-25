"""Screenshot understanding with Gemini vision.

Each PNG is an internal admin screen (customer console, search inspector,
backup manager, connector console...).  Gemini transcribes every record row it
can see into a fixed JSON schema; deterministic code then maps rows to
resource ids (directly, or through data-catalog aliases such as
"delivery_confirmation_19.pdf" -> object_19) and turns them into Observations.
Results are cached, so a rerun costs nothing.
"""
from __future__ import annotations

import json
import re
from typing import Dict, List

from .data import DATASET, REPO_ROOT, EMAIL_RE, norm_email, norm_phone, parse_time, system_for
from .evidence import Obs
from .llm import VISION_MODEL, GeminiClient

VISION_CACHE = REPO_ROOT / "code" / "cache" / "vision_extractions.json"

PROMPT = """This is a screenshot of an internal admin tool at an online shop.
Transcribe every data record visible on the screen (table rows AND the detail
panel on the right).  For each record give:
- label: the record's id or name exactly as shown (e.g. "search_428",
  "backup_9287", "delivery_confirmation_19.pdf", "ORD-20265762", "user_17")
- resource_id: an id of the form <word>_<digits> if one is shown for the record
  (e.g. account_5762, support_1034, data_flow_1121); otherwise ""
- emails, user_refs (user_<digits>), names, phones visible on that record
- status_text: any status/health/state words shown for it (e.g. "Healthy",
  "Active", "Retained reference", "Restore blocked", "Delivered")
- restore: for backup archives, "ALLOWED" if it can be restored, "BLOCKED" if
  restore is blocked/denied, else "UNKNOWN"
- direct_identifiers_shown: true if a name, email or phone is displayed for it
Also give screen_title and the capture timestamp text if shown.
Only transcribe what is visible; never invent values."""

SCHEMA = {
    "type": "OBJECT",
    "properties": {
        "screen_title": {"type": "STRING"},
        "captured_text": {"type": "STRING"},
        "records": {
            "type": "ARRAY",
            "items": {
                "type": "OBJECT",
                "properties": {
                    "label": {"type": "STRING"},
                    "resource_id": {"type": "STRING"},
                    "emails": {"type": "ARRAY", "items": {"type": "STRING"}},
                    "user_refs": {"type": "ARRAY", "items": {"type": "STRING"}},
                    "names": {"type": "ARRAY", "items": {"type": "STRING"}},
                    "phones": {"type": "ARRAY", "items": {"type": "STRING"}},
                    "status_text": {"type": "STRING"},
                    "restore": {"type": "STRING", "enum": ["ALLOWED", "BLOCKED", "UNKNOWN"]},
                    "direct_identifiers_shown": {"type": "BOOLEAN"},
                },
                "required": ["label", "resource_id", "emails", "user_refs", "names",
                             "status_text", "restore", "direct_identifiers_shown"],
            },
        },
    },
    "required": ["screen_title", "records"],
}

RID_RE = re.compile(r"\b(?:account|search|support|analytics|export|data_flow|backup|audit_record|"
                    r"tombstone|marketing|object|legal_hold|cache|email_delivery)_\d+\b")


def extract_images(client: GeminiClient, manifest: Dict[str, Dict[str, str]]) -> Dict[str, dict]:
    """file_id -> Gemini transcription.

    Calls always go through the client (whose response cache makes reruns free
    but still accounts their tokens); the readable transcription file is a
    fallback for offline runs and a human-reviewable artifact.
    """
    saved: Dict[str, dict] = {}
    if VISION_CACHE.exists():
        saved = json.loads(VISION_CACHE.read_text(encoding="utf-8"))
    out: Dict[str, dict] = {}
    for file_id, meta in sorted(manifest.items()):
        if not meta["file_path"].lower().endswith(".png"):
            continue
        try:
            out[file_id] = client.json_call(PROMPT, SCHEMA, "image_extraction",
                                            images=[DATASET / meta["file_path"]],
                                            model=VISION_MODEL)
        except Exception as exc:
            if file_id in saved:
                out[file_id] = saved[file_id]
            else:
                out.setdefault("_errors", {})[file_id] = str(exc)[:300]
    VISION_CACHE.parent.mkdir(parents=True, exist_ok=True)
    VISION_CACHE.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")
    return {k: v for k, v in out.items() if not k.startswith("_")}


def catalog_aliases(activities, strict: bool = True) -> Dict[str, str]:
    """alias shown in UIs/documents -> resource id, from data-catalog link events.

    strict=True (substring search in documents) keeps only distinctive display
    names; strict=False (exact screenshot labels) also allows a bare user
    reference, e.g. a reference-registry screen titled "user_17".
    """
    aliases: Dict[str, str] = {}
    for a in activities:
        if a.event_type != "LINK_RESOURCE_IDENTITY":
            continue
        m = re.search(r"\b" + re.escape(a.resource_id) + r" \(([^)]+)\)", a.details)
        alias = m.group(1).strip().lower() if m else ""
        # Only distinctive display names (file names, statement numbers) are
        # usable aliases; a bare id or user reference would match everywhere.
        if alias and alias != a.resource_id and not (strict and re.fullmatch(r"user_\d+", alias)):
            aliases[alias] = a.resource_id
    return aliases


def vision_to_obs(extractions: Dict[str, dict], manifest, aliases: Dict[str, str] = None,
                  catalog_rids=frozenset()) -> List[Obs]:
    """Screen rows -> Observations.

    When a screen shows a record the data catalog links to a subject, that
    record is the screen's subject of record; the other rows are context
    (filter results, neighbouring customers) and may describe state but do not
    establish ownership on their own.
    """
    aliases = aliases or {}
    out: List[Obs] = []
    for file_id, ext in extractions.items():
        captured = parse_time(manifest[file_id]["captured_at"])
        screen: List[Obs] = []
        for rec in ext.get("records", []):
            label = (rec.get("label") or "").strip()
            rid = (rec.get("resource_id") or "").strip().lower()
            if not RID_RE.fullmatch(rid or "-"):
                found = RID_RE.findall(label.lower())
                rid = found[0] if found else aliases.get(label.lower(), "")
            if not rid:
                continue
            emails = {norm_email(e) for e in rec.get("emails", []) if EMAIL_RE.fullmatch(e.strip())}
            refs = {r.lower() for r in rec.get("user_refs", []) if re.fullmatch(r"user_\d+", r.lower())}
            names = {"name:" + n.strip().lower() for n in rec.get("names", []) if n.strip()}
            phones = {"phone:" + norm_phone(p) for p in rec.get("phones", []) if norm_phone(p)}
            direct = emails | phones | (names if rec.get("direct_identifiers_shown") else set())
            obs = Obs(file_id, captured, captured, system_for(rid) or "", rid, True,
                      direct_ids=direct, user_refs=refs, link_keys=emails | refs | phones,
                      status=rec.get("status_text"), source="vision")
            status = (rec.get("status_text") or "").lower()
            if obs.system == "integration_service":
                obs.flow_enabled = not any(w in status for w in ("disabled", "paused", "stopped"))
            if obs.system == "backup_service":
                restore = rec.get("restore", "UNKNOWN")
                obs.restore_allowed = False if restore == "BLOCKED" else True
            if obs.system in ("object_storage", "support_platform") and label.lower().endswith(".pdf"):
                obs.hints.add("attachment")
            screen.append(obs)
        if any(o.resource_id in catalog_rids for o in screen):
            for o in screen:
                if o.resource_id not in catalog_rids:
                    o.user_refs = set()
                    o.link_keys = set()
                    o.direct_ids = {d for d in o.direct_ids if not d.startswith("name:")}
        out.extend(screen)
    return out
