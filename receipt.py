from __future__ import annotations

from typing import Any

from .models import Receipt
from .utils import new_id, now_iso, sha256_text, stable_dumps


def create_receipt(
    *,
    type: str,
    actor: str,
    summary: str,
    source: str,
    metadata: dict[str, Any] | None = None,
    timestamp: str | None = None,
) -> Receipt:
    resolved_timestamp = now_iso(timestamp)
    payload = {
        "type": type,
        "actor": actor,
        "summary": summary,
        "source": source,
        "metadata": metadata or {},
        "timestamp": resolved_timestamp,
    }
    return Receipt(
        id=new_id("receipt"),
        type=type,
        actor=actor,
        summary=summary,
        source=source,
        timestamp=resolved_timestamp,
        hash=sha256_text(stable_dumps(payload)),
        metadata=metadata or {},
    )
