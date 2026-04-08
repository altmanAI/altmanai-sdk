from __future__ import annotations

from typing import Any

from .models import AINetEvent
from .utils import new_id, now_iso


def emit_event(
    *,
    name: str,
    source: str,
    payload: Any,
    timestamp: str | None = None,
) -> AINetEvent:
    return AINetEvent(
        id=new_id("event"),
        name=name,
        source=source,
        timestamp=now_iso(timestamp),
        payload=payload,
    )
