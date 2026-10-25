"""Deletion policy: category inference, rule lookup, and step vocabulary.

`deletion_rules.csv` is read at runtime; this module only decides which
category a resource belongs to and what each rule action means in terms of
FINDING / REMEDIATION / VERIFICATION operations.
"""
from __future__ import annotations

from typing import Dict, List, Optional

from .evidence import Obs

# Operation order inside each phase, exactly as listed in the problem statement.
OPERATION_ORDER = [
    "REPORT_REMAINING_RECORD", "REPORT_EXPOSED_PII", "REPORT_ACTIVE_DATA_FLOW", "REPORT_RESTORE_RISK",
    "DISABLE_DATA_FLOW", "BLOCK_RESTORE", "DELETE_RECORD", "REDACT_RECORD", "ANONYMIZE_RECORD",
    "VERIFY_RECORD_ABSENT", "VERIFY_RECORD_PRESENT", "VERIFY_RECORD_REDACTED",
    "VERIFY_RECORD_ANONYMIZED", "VERIFY_DATA_FLOW_DISABLED", "VERIFY_RESTORE_BLOCKED",
]
PHASE_OF = {op: ("FINDING" if op.startswith("REPORT") else
                 "VERIFICATION" if op.startswith("VERIFY") else "REMEDIATION")
            for op in OPERATION_ORDER}
STATE_OF = {
    "REPORT_REMAINING_RECORD": "PRESENT", "REPORT_EXPOSED_PII": "PRESENT",
    "REPORT_ACTIVE_DATA_FLOW": "ACTIVE", "REPORT_RESTORE_RISK": "ACTIVE",
    "DISABLE_DATA_FLOW": "DISABLED", "BLOCK_RESTORE": "BLOCKED", "DELETE_RECORD": "ABSENT",
    "REDACT_RECORD": "REDACTED", "ANONYMIZE_RECORD": "ANONYMIZED",
    "VERIFY_RECORD_ABSENT": "ABSENT", "VERIFY_RECORD_PRESENT": "PRESENT",
    "VERIFY_RECORD_REDACTED": "REDACTED", "VERIFY_RECORD_ANONYMIZED": "ANONYMIZED",
    "VERIFY_DATA_FLOW_DISABLED": "DISABLED", "VERIFY_RESTORE_BLOCKED": "BLOCKED",
}
PHASE_ORDER = {"FINDING": 0, "REMEDIATION": 1, "VERIFICATION": 2}

SYSTEM_CATEGORY = {
    "account_service": "USER_PROFILE",
    "search_service": "SEARCH_INDEX_ENTRY",
    "cache_service": "CACHE_ENTRY",
    "support_platform": "SUPPORT_MESSAGE",
    "analytics_platform": "ANALYTICS_PROFILE",
    "export_service": "USER_EXPORT",
    "marketing_platform": "MARKETING_PROFILE",
    "email_delivery_service": "EMAIL_DELIVERY_LOG",
    "security_service": "SECURITY_AUDIT_LOG",
    "legal_service": "LEGAL_HOLD_RECORD",
    "backup_service": "BACKUP_ARCHIVE",
    "identity_service": "ACCOUNT_TOMBSTONE",
    "integration_service": "DATA_FLOW",
    "object_storage": "SUPPORT_ATTACHMENT",
}


class Policy:
    def __init__(self, rules: List[Dict[str, str]]):
        self.action: Dict[str, str] = {r["data_category"]: r["required_action"] for r in rules}
        self.condition: Dict[str, str] = {r["data_category"]: r["condition"] for r in rules}

    def category(self, system: str, observations: List[Obs]) -> str:
        hints = set()
        explicit: Optional[str] = None
        for o in observations:
            hints |= o.hints
            if o.category and o.category not in ("DATA_FLOW",):
                explicit = o.category
        if system == "support_platform":
            if "attachment" in hints or explicit == "SUPPORT_ATTACHMENT":
                return "SUPPORT_ATTACHMENT"
            if "contact" in hints:
                return "SECONDARY_IDENTIFIER"
            return "SUPPORT_MESSAGE"
        if system == "analytics_platform" and "marketing" in hints:
            return "MARKETING_PROFILE"
        if explicit and explicit in self.action and system not in SYSTEM_CATEGORY:
            return explicit
        return SYSTEM_CATEGORY.get(system, explicit or "USER_PROFILE")

    def required_action(self, category: str) -> str:
        if category == "DATA_FLOW":
            return "DISABLE"
        return self.action.get(category, "DELETE")
