from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from uuid import uuid4


def now_iso(value: str | None = None) -> str:
    if value:
        return value
    return datetime.now(tz=timezone.utc).isoformat().replace("+00:00", "Z")


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4()}"


def stable_dumps(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()
