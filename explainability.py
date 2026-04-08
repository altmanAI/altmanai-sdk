from __future__ import annotations

from .models import ExplainabilityRecord
from .utils import now_iso


def create_explainability_record(
    *,
    decision: str,
    reason: str,
    evidence: list[str] | None = None,
    actor: str | None = None,
    confidence: float | None = None,
    timestamp: str | None = None,
) -> ExplainabilityRecord:
    return ExplainabilityRecord(
        decision=decision,
        reason=reason,
        evidence=evidence or [],
        actor=actor,
        confidence=confidence,
        timestamp=now_iso(timestamp),
    )
