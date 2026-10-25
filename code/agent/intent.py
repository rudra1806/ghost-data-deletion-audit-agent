"""Does the request text actually authorize deletion?

Two independent signals:
  * Gemini reads every distinct request text (batched, any language) and
    returns a structured verdict with a request type and rationale;
  * a deterministic multilingual rule set (deletion verbs + explicit
    non-deletion / negation markers) acts as a cross-check and as the fallback
    when no API key is configured.
Disagreements are surfaced in the run trace so they can be reviewed.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from typing import Dict, List, Optional

from .llm import GeminiClient

DELETION_PATTERNS = [
    r"\bdelet", r"\beras", r"\bremov", r"\bclose (my|this|the) account", r"\bis gone\b",
    r"\bclosed? .*account permanently", r"account[- ]deletion", r"\bdeletion\b",
    r"elimina", r"borrar", r"supresi[oó]n", r"suppression", r"supprimer", r"effacer",
    r"exclus[aã]o", r"excluir", r"apagar", r"l[öo]sch", r"cancellare", r"eliminazione",
    r"verwijder", r"削除", r"삭제", r"删除", r"刪除", r"удал",
]
NON_DELETION_PATTERNS = [
    r"not asking for deletion", r"not a request to (erase|delete)", r"\bdo not (close|delete)",
    r"don'?t (delete|close)", r"without removing", r"leave (the|my) (account|profile)",
    r"keep the account", r"continue using", r"marketing lists only", r"stop the promotional",
    r"send me a copy", r"need a copy", r"download my", r"portable format", r"what personal information you hold",
    r"reset(ting)? the login", r"\bcorrect it\b", r"misspelled", r"change the email",
    r"replace it with the new", r"still use it", r"still want receipts",
]

REQUEST_TYPES = ["DELETION", "ACCESS", "PORTABILITY", "CORRECTION", "MARKETING_OPT_OUT",
                 "ACCOUNT_RECOVERY", "OTHER"]

SYSTEM_PROMPT = """You are a privacy-operations analyst at an e-commerce company.
For each customer message decide whether it AUTHORIZES DELETION of the customer's
account / personal data (GDPR Art.17 style erasure or permanent account closure).

Rules:
- Messages may be in any language; judge the meaning, not keywords.
- Requests for access/copy, export/download, correction/update, login help,
  marketing opt-out ("only"), or anything that says to keep the account are NOT deletion.
- Negations matter: "not asking for deletion", "do not close the account" => not deletion.
- A request to delete the account that also allows some records to be retained
  (backups, security logs, anonymous statistics) IS still deletion.
- A follow-up on the customer's own deletion ("verify my account was deleted",
  "check whether my data has been removed", "my request shows failed, inspect the
  systems", "confirm the profile is gone") IS deletion: it asks the company to
  confirm and, where needed, complete an erasure the customer requested.
Return one verdict per message id."""

SCHEMA = {
    "type": "ARRAY",
    "items": {
        "type": "OBJECT",
        "properties": {
            "id": {"type": "STRING"},
            "authorizes_deletion": {"type": "BOOLEAN"},
            "request_type": {"type": "STRING", "enum": REQUEST_TYPES},
            "language": {"type": "STRING"},
            "rationale": {"type": "STRING"},
        },
        "required": ["id", "authorizes_deletion", "request_type", "language", "rationale"],
    },
}


@dataclass
class IntentVerdict:
    authorizes_deletion: bool
    request_type: str
    source: str
    rule_verdict: bool
    rationale: str = ""
    language: str = ""

    @property
    def disagreement(self) -> bool:
        return self.authorizes_deletion != self.rule_verdict


def rule_verdict(text: str) -> bool:
    low = text.lower()
    if any(re.search(p, low) for p in NON_DELETION_PATTERNS):
        return False
    return any(re.search(p, low) for p in DELETION_PATTERNS)


def text_id(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


class IntentClassifier:
    def __init__(self, client: Optional[GeminiClient], batch_size: int = 20):
        self.client = client
        self.batch_size = batch_size
        self.errors: List[str] = []

    def classify(self, texts: List[str]) -> Dict[str, IntentVerdict]:
        distinct = sorted(set(texts))
        llm: Dict[str, dict] = {}
        if self.client and self.client.available:
            for i in range(0, len(distinct), self.batch_size):
                batch = distinct[i:i + self.batch_size]
                prompt = "Classify these customer messages:\n\n" + "\n\n".join(
                    f"id={text_id(t)}\nmessage: {t}" for t in batch)
                try:
                    rows = self.client.json_call(prompt, SCHEMA, "intent_classification",
                                                 system=SYSTEM_PROMPT)
                    for row in rows:
                        llm[row["id"]] = row
                except Exception as exc:  # fall back to rules for this batch
                    self.errors.append(f"intent batch {i}: {exc}")
        out: Dict[str, IntentVerdict] = {}
        for t in distinct:
            rv = rule_verdict(t)
            row = llm.get(text_id(t))
            if row is not None:
                out[t] = IntentVerdict(bool(row["authorizes_deletion"]), row["request_type"],
                                       "gemini", rv, row.get("rationale", ""),
                                       row.get("language", ""))
            else:
                out[t] = IntentVerdict(rv, "DELETION" if rv else "OTHER", "rules", rv)
        return out
