"""Evidence ingestion: every supplied file becomes a list of Observations.

An Observation is one grounded statement of the form "at time T, file F showed
resource R in system S in this state, carrying these identifiers".  A Scope is
a full point-in-time listing of a system/collection, which lets the agent prove
absence for a resource the listing does not contain.

Parsers are format-specific (SQL, JSON families, seven log dialects, the shift
handover, PDFs) but all of them emit the same two types, so the reasoner never
cares where a fact came from.  Images are handled by vision.py and converted
into the same shape.
"""
from __future__ import annotations

import json
import re
import sqlite3
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Iterable, List, Optional, Set, Tuple

from .data import (DATASET, EMAIL_RE, HASH_RE, USER_REF_RE, norm_email, norm_phone,
                   parse_time, system_for)

NAME_KEYS = {"full_name", "name", "requester_name", "display_name"}
PHONE_KEYS = {"phone", "requester_phone", "owner_phone"}
# Keys whose value names the subject a lookup was run for (not a field on the
# record itself).  They link a resource to a subject without implying the
# record still exposes that identifier.
LOOKUP_KEYS = {"lookup_key", "subject_key", "subject_ref", "match_key", "scan_key",
               "correlation_key", "owner_key", "lookup_value", "query", "subject_selector"}
FREE_TEXT_KEYS = {"message_text", "message_excerpt", "details"}

PRESENT_RESULTS = {"FOUND", "IDENTIFIABLE", "ANONYMIZED", "REDACTED", "ACTIVE",
                   "DISABLED", "BLOCKED", "hit"}
ABSENT_RESULTS = {"NOT_FOUND", "miss", "ABSENT", "DELETED_CONFIRMED"}


@dataclass
class Obs:
    evidence_id: str
    captured_at: datetime          # manifest capture time (citation eligibility)
    observed_at: datetime          # when the stated fact was true
    system: str
    resource_id: str
    present: Optional[bool]        # None when the source could not tell (e.g. 503)
    direct_ids: Set[str] = field(default_factory=set)   # name/email/phone/hash still on record
    user_refs: Set[str] = field(default_factory=set)    # stable user_id references on record
    link_keys: Set[str] = field(default_factory=set)    # tokens tying record to a subject
    flow_enabled: Optional[bool] = None
    restore_allowed: Optional[bool] = None
    category: Optional[str] = None  # explicit category / record type hint
    status: Optional[str] = None    # explicit status word from the source
    hints: Set[str] = field(default_factory=set)        # e.g. attachment, marketing
    source: str = ""

    @property
    def exposes_direct(self) -> bool:
        return bool(self.direct_ids)


@dataclass
class Scope:
    """A complete listing of one system at one time (proves absence)."""
    evidence_id: str
    captured_at: datetime
    observed_at: datetime
    system: str
    resource_ids: Set[str]


@dataclass
class EvidenceStore:
    observations: List[Obs] = field(default_factory=list)
    scopes: List[Scope] = field(default_factory=list)
    by_resource: Dict[str, List[Obs]] = field(default_factory=lambda: defaultdict(list))
    by_key: Dict[str, Set[str]] = field(default_factory=lambda: defaultdict(set))
    texts: Dict[str, str] = field(default_factory=dict)   # file_id -> raw text (for search tools)

    def add(self, obs: Obs) -> None:
        if not obs.resource_id or not obs.system:
            return
        self.observations.append(obs)
        self.by_resource[obs.resource_id].append(obs)
        for key in obs.link_keys | obs.direct_ids | obs.user_refs:
            self.by_key[key].add(obs.resource_id)


# --------------------------------------------------------------------------
# identifier extraction


def classify_value(key: str, value) -> Tuple[Set[str], Set[str]]:
    """Return (direct identifier tokens, user_ref tokens) for one field."""
    direct: Set[str] = set()
    refs: Set[str] = set()
    if value is None or isinstance(value, (bool, int, float)):
        return direct, refs
    text = str(value).strip()
    if not text or text.lower() in ("null", "none", "[redacted]"):
        return direct, refs
    low = text.lower()
    if USER_REF_RE.match(low):
        refs.add(low)
    elif HASH_RE.match(low):
        direct.add(low)
    elif key in PHONE_KEYS:
        direct.add("phone:" + norm_phone(text))
    elif key in NAME_KEYS:
        direct.add("name:" + low)
    else:
        for email in EMAIL_RE.findall(text):
            direct.add(norm_email(email))
    return direct, refs


def extract_ids(record: dict, skip: Iterable[str] = ()) -> Tuple[Set[str], Set[str], Set[str]]:
    """Walk a record; return (direct ids, user refs, lookup-only keys)."""
    direct: Set[str] = set()
    refs: Set[str] = set()
    lookups: Set[str] = set()
    skip = set(skip)

    def walk(obj, key=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in skip:
                    continue
                walk(v, k)
        elif isinstance(obj, list):
            for v in obj:
                walk(v, key)
        else:
            d, r = classify_value(key, obj)
            if key in LOOKUP_KEYS:
                lookups.update(d | r)
            else:
                direct.update(d)
                refs.update(r)

    walk(record)
    return direct, refs, lookups


# --------------------------------------------------------------------------
# record -> observation (shared by SQL and JSON snapshots)

COLLECTION_HINTS = {
    "ticket_attachments": "attachment",
    "support_conversations": "message",
    "support_records": "message",
    "retained_order_records": "legal_hold",
    "deleted_customer_references": "tombstone",
}


def record_obs(evidence_id: str, captured: datetime, observed: datetime, system: str,
               record: dict, collection: str = "", source: str = "") -> Optional[Obs]:
    rid = record.get("resource_id")
    if not rid:
        return None
    system = system or system_for(rid) or ""
    skip = {"resource_id", "archive_key", "archive_path", "object_key", "file_name",
            "integrity_seal", "account_status", "updated_at"}
    direct, refs, lookups = extract_ids(record, skip)
    obs = Obs(evidence_id=evidence_id, captured_at=captured, observed_at=observed,
              system=system, resource_id=rid, present=True, direct_ids=direct,
              user_refs=refs, link_keys=direct | refs | lookups, source=source)
    hint = COLLECTION_HINTS.get(collection)
    if hint:
        obs.hints.add(hint)
    if "uploaded_by" in record or "file_name" in record and system == "support_platform":
        obs.hints.add("attachment")
    if "email_opt_in" in record or "marketing" in collection:
        obs.hints.add("marketing")
    if "enabled" in record:
        obs.flow_enabled = _truthy(record["enabled"])
    if "restore_allowed" in record:
        obs.restore_allowed = _truthy(record["restore_allowed"])
    if "download_available" in record:
        obs.hints.add("download_available" if _truthy(record["download_available"]) else "download_expired")
    status = record.get("account_status")
    if status:
        obs.status = str(status)
    return obs


def _truthy(value) -> Optional[bool]:
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    text = str(value).strip().lower()
    if text in ("1", "true", "yes", "allow", "enabled"):
        return True
    if text in ("0", "false", "no", "deny", "disabled"):
        return False
    return None


def lookup_obs(evidence_id: str, captured: datetime, observed: datetime, system: str,
               rid: str, record_type: str, result: str, subject: str, source: str) -> Obs:
    """A lookup/inspection row such as `account_x USER_PROFILE NOT_FOUND alice@...`."""
    system = system or system_for(rid) or ""
    keys: Set[str] = set()
    d, r = classify_value("lookup_key", subject)
    keys |= d | r
    obs = Obs(evidence_id=evidence_id, captured_at=captured, observed_at=observed,
              system=system, resource_id=rid, present=None, link_keys=keys,
              category=record_type or None, status=result, source=source)
    apply_status_word(obs, result, subject)
    return obs


def apply_status_word(obs: Obs, result: str, subject: str = "") -> None:
    """Translate a status word (FOUND, IDENTIFIABLE, ACTIVE...) into state."""
    result = (result or "").strip()
    up = result.upper()
    if up in ("NOT_FOUND", "MISS", "ABSENT"):
        obs.present = False
    elif up in PRESENT_RESULTS or result in PRESENT_RESULTS:
        obs.present = True
    if up == "ACTIVE":
        if obs.system == "integration_service" or obs.category == "DATA_FLOW":
            obs.flow_enabled = True
        if obs.system == "backup_service" or obs.category == "BACKUP_ARCHIVE":
            obs.restore_allowed = True
    elif up == "DISABLED":
        obs.flow_enabled = False
    elif up == "BLOCKED":
        obs.restore_allowed = False
    elif up in ("IDENTIFIABLE", "FOUND") and subject:
        d, r = classify_value("email", subject)
        # The status line shows the subject's identifier on the record itself.
        if up == "IDENTIFIABLE" or obs.category in ("SEARCH_INDEX_ENTRY", "USER_PROFILE",
                                                     "SUPPORT_ATTACHMENT", "USER_EXPORT"):
            obs.direct_ids |= d
        obs.user_refs |= r
    elif up in ("ANONYMIZED",):
        obs.direct_ids = set()
        obs.user_refs = set()
    elif up == "REDACTED":
        obs.direct_ids = set()
        d, r = classify_value("email", subject)
        obs.user_refs |= r


# --------------------------------------------------------------------------
# SQL snapshots

TYPED_TABLE_SYSTEM = {
    "customer_profiles": "account_service",
    "customer_profiles_primary": "account_service",
    "customer_profiles_failover_replica": "account_service",
    "customer_search_documents": "search_service",
    "search_documents_primary": "search_service",
    "customer_analytics_profiles": "analytics_platform",
    "support_records": "support_platform",
    "customer_exports": "export_service",
    "connector_subscriptions": "integration_service",
    "backup_restore_entries": "backup_service",
    "security_audit_records": "security_service",
}


def parse_sql(store: EvidenceStore, file_id: str, path, captured: datetime) -> None:
    text = path.read_text(encoding="utf-8")
    store.texts[file_id] = text
    db = sqlite3.connect(":memory:")
    db.executescript(text)
    db.row_factory = sqlite3.Row
    tables = [r[0] for r in db.execute("select name from sqlite_master where type='table'")]
    scope_systems: Set[str] = set()
    listed: Dict[str, Set[str]] = defaultdict(set)
    if "snapshot_scope" in tables:
        for row in db.execute("select origin_system from snapshot_scope"):
            scope_systems.add(row[0])
    for table in tables:
        if table == "snapshot_scope":
            continue
        cols = [r[1] for r in db.execute(f"pragma table_info({table})")]
        for row in db.execute(f"select * from {table}"):
            row = dict(row)
            if "record_json" in cols:
                record = json.loads(row["record_json"])
                system = row.get("origin_system") or ""
                collection = row.get("collection_name", "")
            else:
                record = dict(row)
                system = TYPED_TABLE_SYSTEM.get(table, "")
                collection = table
            obs = record_obs(file_id, captured, captured, system, record, collection,
                             source=f"sql:{table}")
            if obs is None:
                continue
            store.add(obs)
            listed[obs.system].add(obs.resource_id)
            if "snapshot_scope" not in tables:
                scope_systems.add(obs.system)
    for system in scope_systems:
        store.scopes.append(Scope(file_id, captured, captured, system, listed.get(system, set())))


# --------------------------------------------------------------------------
# JSON families


def parse_json(store: EvidenceStore, file_id: str, path, captured: datetime) -> None:
    text = path.read_text(encoding="utf-8")
    store.texts[file_id] = text
    doc = json.loads(text)
    if "snapshots" in doc:                       # records-assurance bundle
        for snap in doc["snapshots"]:
            when = parse_time(snap["captured_at"])
            system = snap.get("data_store", "")
            coll = snap.get("collection", "")
            if coll == "operational_record_history":
                for rec in snap["records"]:
                    store.add(lookup_obs(file_id, captured, parse_time(rec["recorded_at"]),
                                         rec.get("system", ""), rec["resource_id"],
                                         rec.get("record_type", ""), rec.get("result", ""),
                                         rec.get("lookup_value", ""), "json:history"))
                continue
            ids = set()
            for rec in snap["records"]:
                obs = record_obs(file_id, captured, when, system, rec, coll, "json:bundle")
                if obs:
                    store.add(obs)
                    ids.add(obs.resource_id)
            store.scopes.append(Scope(file_id, captured, when, system, ids))
    elif "service_exports" in doc:               # per-service readback export
        for system, colls in doc["service_exports"].items():
            for coll, recs in colls.items():
                for rec in recs:
                    parse_export_record(store, file_id, captured, system, coll, rec)
    elif "records" in doc and doc["records"] and "record_type" in doc["records"][0]:
        for rec in doc["records"]:                # lookup ledgers
            store.add(lookup_obs(file_id, captured, parse_time(rec["recorded_at"]),
                                 rec.get("system", ""), rec["resource_id"],
                                 rec.get("record_type", ""), rec.get("result", ""),
                                 rec.get("subject_reference", ""), "json:ledger"))
    elif "records" in doc:                       # single collection capture
        when = parse_time(doc.get("captured_at") or doc.get("exported_at"))
        coll = doc.get("collection", "")
        system = {"analytics_identity_store": "analytics_platform",
                  "user_export_store": "export_service"}.get(doc.get("source", ""), "")
        for rec in doc["records"]:
            obs = record_obs(file_id, captured, when, system, rec, coll, "json:collection")
            if obs:
                store.add(obs)


def parse_export_record(store, file_id, captured, system, coll, rec) -> None:
    when = parse_time(rec["observed_at"]) if rec.get("observed_at") else captured
    if coll == "index_queries":
        docs = (rec.get("hits") or {}).get("documents") or []
        _, _, qkeys = extract_ids({"query": rec.get("query")})
        for d in docs:
            obs = record_obs(file_id, captured, when, system, d, coll, "json:export")
            if obs:
                obs.link_keys |= qkeys
                store.add(obs)
        return
    if coll == "profile_lookups":
        profile = rec.get("profile")
        code = rec.get("status_code")
        if profile:
            obs = record_obs(file_id, captured, when, system,
                             dict(profile, resource_id=rec["resource_id"]), coll, "json:export")
        else:
            obs = Obs(file_id, captured, when, system, rec["resource_id"], None, source="json:export")
        obs.present = True if code == 200 else False if code == 404 else None
        store.add(obs)
        return
    obs = record_obs(file_id, captured, when, system, rec, coll, "json:export")
    if obs:
        if coll in ("tickets",) and "attachment" in json.dumps(rec).lower():
            obs.hints.add("attachment")
        store.add(obs)


# --------------------------------------------------------------------------
# logs (seven dialects, one tokenizer)

TS_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)")
KV_RE = re.compile(r'"?([A-Za-z_][\w]*)"?\s*[=:]\s*(?:"((?:[^"\\]|\\.)*)"|([^\s",|}]+))')
TRACE_RE = re.compile(r"\b((?:tr|rb|rp)-[\w-]+)")
KNOWN_SERVICES = {"account_service", "search_service", "support_platform", "analytics_platform",
                  "export_service", "integration_service", "backup_service", "security_service",
                  "identity_service", "marketing_platform", "object_storage", "legal_service",
                  "email_delivery_service", "cache_service", "profile_service", "support_replica",
                  "attachment_preview"}
SERVICE_ALIAS = {"profile_service": "account_service", "support_replica": "support_platform"}
LOG_LINK_KEYS = LOOKUP_KEYS | {"subject_reference", "customer_reference", "matched_value",
                               "customer_email", "email", "requester_email", "owner_email"}


def tokenize_line(line: str) -> Tuple[Optional[datetime], Dict[str, str], Optional[str], str]:
    m = TS_RE.match(line)
    if not m:
        return None, {}, None, ""
    ts = parse_time(m.group(1))
    body = line[m.end():].replace('\\"', '"')
    kv: Dict[str, str] = {}
    for k, quoted, bare in KV_RE.findall(body):
        kv.setdefault(k, quoted if quoted else bare)
    trace = kv.get("trace_id") or kv.get("requestId")
    if not trace:
        t = TRACE_RE.search(body)
        trace = t.group(1) if t else None
    service = kv.get("service") or kv.get("logger") or kv.get("function") or ""
    if not service:
        for token in re.findall(r"[a-z_]+", body[:120]):
            if token in KNOWN_SERVICES:
                service = token
                break
    event = kv.get("event", "")
    if not event:
        em = re.search(r"\] (\w+): ", body) or re.search(r"\| (\w+) \| instance", body)
        if em:
            event = em.group(1)
    kv["_event"] = event
    return ts, kv, trace, SERVICE_ALIAS.get(service, service)


def parse_log(store: EvidenceStore, file_id: str, path, captured: datetime) -> None:
    text = path.read_text(encoding="utf-8")
    store.texts[file_id] = text
    lines = [tokenize_line(l) for l in text.splitlines()]
    trace_keys: Dict[str, Set[str]] = defaultdict(set)
    for ts, kv, trace, service in lines:
        if ts is None or not trace:
            continue
        for k in LOG_LINK_KEYS:
            if k in kv:
                d, r = classify_value("lookup_key", kv[k])
                trace_keys[trace] |= d | r
    for ts, kv, trace, service in lines:
        if ts is None or "resource_id" not in kv:
            continue
        rid = kv["resource_id"]
        system = kv.get("system") or system_for(rid) or service
        if system in SERVICE_ALIAS:
            system = SERVICE_ALIAS[system]
        obs = Obs(file_id, captured, ts, system, rid, None, source="log:" + kv["_event"])
        if trace:
            obs.link_keys |= trace_keys.get(trace, set())
        interpret_log_fields(obs, kv)
        store.add(obs)


def interpret_log_fields(obs: Obs, kv: Dict[str, str]) -> None:
    event = kv.get("_event", "")
    if event.endswith("_started") and not any(k in kv for k in ("rows", "result", "enabled")):
        # A started line only names the resource; state comes from the completion.
        obs.present = None
    if event.endswith("_completed") or event in ("analytics_profile_read", "message_read",
                                                   "retained_order_loaded"):
        # A completed read that returned a record body means the record exists.
        if not any(k in kv for k in ("rows", "result", "available", "http_status")):
            obs.present = True
    if kv.get("http_status") == "503":
        obs.present = None
        return
    if "rows" in kv:
        obs.present = kv["rows"] != "0"
    if kv.get("http_status") == "404":
        obs.present = False
    elif kv.get("http_status") == "200":
        obs.present = True
    if "record_type" in kv:
        obs.category = kv["record_type"]
    if "result" in kv:
        subject = kv.get("subject_reference", "")
        apply_status_word(obs, kv["result"], subject)
        if subject:
            d, r = classify_value("lookup_key", subject)
            obs.link_keys |= d | r
    if "enabled" in kv:
        obs.flow_enabled = _truthy(kv["enabled"])
        obs.present = True
    if "restore_allowed" in kv:
        obs.restore_allowed = _truthy(kv["restore_allowed"])
        obs.present = True
    if kv.get("eligible") == "true" and kv.get("deletion_block") == "false":
        obs.restore_allowed = True
        obs.present = True
    if kv.get("decision") == "deny":
        obs.restore_allowed = False
        obs.present = True
    if kv.get("decision") == "allow":
        obs.restore_allowed = True
        obs.present = True
    if "available" in kv:
        obs.present = kv["available"] == "true"
    if kv.get("marker_found") == "false":
        obs.present = True
    if "matched_value" in kv and kv.get("detector") == "direct_identifier":
        obs.present = True
        d, r = classify_value("email", kv["matched_value"])
        obs.direct_ids |= d
        obs.user_refs |= r
    if "file" in kv or "attachment" in event:
        obs.hints.add("attachment")
    if "email_opt_in" in kv or "contact_lookup" in event:
        obs.hints.add("marketing")
    if "contact_query" in event or kv.get("source") == "legacy_contact_index":
        obs.hints.add("contact")
    if kv.get("direct_identifiers") == "0":
        obs.present = True
    if kv.get("message_text") == "[REDACTED]":
        obs.present = True
    # Record fields echoed on the line describe what the record still holds.
    for key, value in kv.items():
        if key in ("email", "phone", "email_hash", "requester_email", "requester_name",
                   "requester_phone", "customer_email", "owner_email", "display_name"):
            d, r = classify_value(key, value)
            obs.direct_ids |= d
            obs.user_refs |= r
            obs.link_keys |= d | r
        elif key in ("customer_reference", "subject_reference") and \
                USER_REF_RE.match(str(value).lower()):
            obs.user_refs.add(str(value).lower())
            obs.link_keys.add(str(value).lower())
    if event in ("audit_record_read_completed",) or obs.system == "security_service":
        if "rows" in kv:
            obs.present = kv["rows"] != "0"


# --------------------------------------------------------------------------
# plain text handover and PDFs

HANDOVER_RE = re.compile(r"^-\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(\S+)\s*\|\s*(.+)$")


def parse_handover(store: EvidenceStore, file_id: str, path, captured: datetime) -> None:
    text = path.read_text(encoding="utf-8")
    store.texts[file_id] = text
    for line in text.splitlines():
        m = HANDOVER_RE.match(line.strip())
        if not m:
            continue
        when, system, rid, category, status, subject = m.groups()
        subject = "" if "no direct identifier" in subject else subject.strip()
        obs = lookup_obs(file_id, captured, parse_time(when), system, rid, category,
                         status, subject, "text:handover")
        if category == "SUPPORT_ATTACHMENT":
            obs.hints.add("attachment")
        store.add(obs)




def parse_pdf(store: EvidenceStore, file_id: str, path, captured: datetime) -> None:
    try:
        import fitz  # PyMuPDF
    except ImportError:  # pragma: no cover - documented dependency
        return
    doc = fitz.open(str(path))
    text = "\n".join(page.get_text() for page in doc)
    store.texts[file_id] = text
    emails = {norm_email(e) for e in EMAIL_RE.findall(text)}
    refs = set(re.findall(r"\buser_\d+\b", text))
    rids = set(re.findall(r"\b(?:support|export|account|audit_record|search|analytics|backup|"
                          r"data_flow|tombstone|legal_hold)_\d+\b", text))
    phones = {"phone:" + norm_phone(p) for p in re.findall(r"\+\d[\d ]{7,}\d", text)}
    for rid in rids:
        obs = Obs(file_id, captured, captured, system_for(rid) or "", rid, True,
                  direct_ids=emails | phones, user_refs=refs, link_keys=emails | refs | phones,
                  source="pdf")
        if "attachment" in text.lower() or ".pdf" in text.lower():
            obs.hints.add("attachment")
        if "retain until" in text.lower():
            obs.direct_ids = set()
        store.add(obs)


# --------------------------------------------------------------------------


def load_evidence(manifest: Dict[str, Dict[str, str]], extra: Iterable[Obs] = ()) -> EvidenceStore:
    """Parse every manifest file; `extra` carries observations from vision."""
    store = EvidenceStore()
    for file_id, meta in sorted(manifest.items()):
        path = DATASET / meta["file_path"]
        captured = parse_time(meta["captured_at"])
        suffix = path.suffix.lower()
        if suffix == ".sql":
            parse_sql(store, file_id, path, captured)
        elif suffix == ".json":
            parse_json(store, file_id, path, captured)
        elif suffix == ".log":
            parse_log(store, file_id, path, captured)
        elif suffix == ".txt":
            parse_handover(store, file_id, path, captured)
        elif suffix == ".pdf":
            parse_pdf(store, file_id, path, captured)
    for obs in extra:
        store.add(obs)
    return store
