from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Receipt:
    id: str
    type: str
    actor: str
    summary: str
    source: str
    timestamp: str
    hash: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class AINetEvent:
    id: str
    name: str
    source: str
    timestamp: str
    payload: Any


@dataclass(slots=True)
class ExplainabilityRecord:
    decision: str
    reason: str
    timestamp: str
    evidence: list[str] = field(default_factory=list)
    actor: str | None = None
    confidence: float | None = None
