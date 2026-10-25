"""Dataset loading, time handling and identifier normalisation.

Everything that touches raw CSV columns lives here so the rest of the agent
works with typed, normalised values.
"""
from __future__ import annotations

import csv
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set

REPO_ROOT = Path(__file__).resolve().parents[2]
DATASET = REPO_ROOT / "dataset"

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
USER_REF_RE = re.compile(r"^user_\d+$")
HASH_RE = re.compile(r"^[0-9a-f]{64}$")

# Resource-id prefix -> owning system.  Used when a source names a resource
# without saying which system holds it (activity rows always say, evidence
# often does not).
PREFIX_SYSTEM = [
    ("audit_record_", "security_service"),
    ("data_flow_", "integration_service"),
    ("email_delivery_", "email_delivery_service"),
    ("legal_hold_", "legal_service"),
    ("tombstone_", "identity_service"),
    ("account_", "account_service"),
    ("search_", "search_service"),
    ("support_", "support_platform"),
    ("analytics_", "analytics_platform"),
    ("export_", "export_service"),
    ("backup_", "backup_service"),
    ("marketing_", "marketing_platform"),
    ("object_", "object_storage"),
    ("cache_", "cache_service"),
]


def system_for(resource_id: str) -> Optional[str]:
    for prefix, system in PREFIX_SYSTEM:
        if resource_id.startswith(prefix):
            return system
    return None


def parse_time(value: str) -> datetime:
    value = value.strip()
    if value.endswith("Z"):
        value = value[:-1] + "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def norm_email(value: str) -> str:
    return value.strip().lower()


def norm_phone(value: str) -> str:
    return re.sub(r"\D", "", value or "")


def read_csv(name: str) -> List[Dict[str, str]]:
    with open(DATASET / name, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


@dataclass
class Request:
    case_id: str
    email: str
    requested_at: datetime
    reported_status: str
    reported_at: datetime
    audit_at: datetime
    request_text: str

    @classmethod
    def from_row(cls, row: Dict[str, str]) -> "Request":
        return cls(
            case_id=row["case_id"],
            email=row["email"],
            requested_at=parse_time(row["requested_at"]),
            reported_status=row["reported_status"],
            reported_at=parse_time(row["reported_at"]),
            audit_at=parse_time(row["audit_at"]),
            request_text=row["request_text"],
        )


@dataclass
class Activity:
    activity_id: str
    event_time: datetime
    event_type: str
    source_system: str
    target_system: str
    resource_id: str
    reported_result: str
    details: str


@dataclass
class Identity:
    """Every identifier a subject has ever used, plus provenance."""

    user_id: str
    names: Set[str] = field(default_factory=set)
    emails: Set[str] = field(default_factory=set)
    phones: Set[str] = field(default_factory=set)
    hashes: Set[str] = field(default_factory=set)
    audit_ids: List[str] = field(default_factory=list)

    def keys(self) -> Set[str]:
        """Normalised tokens used to match evidence to this subject."""
        out = {self.user_id} | self.emails | self.hashes
        out |= {"phone:" + p for p in self.phones if p}
        out |= {"name:" + n for n in self.names if n}
        return out


@dataclass
class Dataset:
    requests: List[Request]
    sample_requests: List[Request]
    identities: Dict[str, Identity]
    email_index: Dict[str, str]
    activities: List[Activity]
    rules: List[Dict[str, str]]
    manifest: Dict[str, Dict[str, str]]


def load_identities() -> (Dict[str, Identity], Dict[str, str]):
    identities: Dict[str, Identity] = {}
    email_index: Dict[str, str] = {}
    for row in read_csv("user_identities.csv"):
        ident = Identity(user_id=row["user_id"])
        ident.names.add(row["name"].strip().lower())
        ident.emails.add(norm_email(row["email"]))
        ident.phones.add(norm_phone(row["phone"]))
        ident.hashes.add(row["email_hash"].strip().lower())
        identities[ident.user_id] = ident
    for row in read_csv("user_audit_log.csv"):
        ident = identities.get(row["user_id"])
        if ident is None:
            continue
        ident.audit_ids.append(row["audit_id"])
        for value in (row["old_value"], row["new_value"]):
            if not value:
                continue
            if row["field_name"] == "email":
                ident.emails.add(norm_email(value))
            elif row["field_name"] == "phone":
                ident.phones.add(norm_phone(value))
            elif row["field_name"] == "email_hash":
                ident.hashes.add(value.strip().lower())
            elif row["field_name"] in ("name", "full_name"):
                ident.names.add(value.strip().lower())
    for ident in identities.values():
        for email in ident.emails:
            # Current snapshot wins over a historical claim on the same address.
            email_index.setdefault(email, ident.user_id)
    for row in read_csv("user_identities.csv"):
        email_index[norm_email(row["email"])] = row["user_id"]
    return identities, email_index


def load_dataset() -> Dataset:
    identities, email_index = load_identities()
    activities = [
        Activity(
            activity_id=r["activity_id"],
            event_time=parse_time(r["event_time"]),
            event_type=r["event_type"],
            source_system=r["source_system"],
            target_system=r["target_system"],
            resource_id=r["resource_id"],
            reported_result=r["reported_result"],
            details=r["details"],
        )
        for r in read_csv("system_activity.csv")
    ]
    return Dataset(
        requests=[Request.from_row(r) for r in read_csv("deletion_requests.csv")],
        sample_requests=[Request.from_row(r) for r in read_csv("sample_deletion_requests.csv")],
        identities=identities,
        email_index=email_index,
        activities=activities,
        rules=read_csv("deletion_rules.csv"),
        manifest={r["file_id"]: r for r in read_csv("evidence_files.csv")},
    )
