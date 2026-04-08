from __future__ import annotations

from .utils import sha256_text, stable_dumps


def hash_artifact(payload: object) -> str:
    return sha256_text(stable_dumps(payload))


def verify_artifact(payload: object, expected_hash: str) -> dict[str, object]:
    actual_hash = hash_artifact(payload)
    return {
        "ok": actual_hash == expected_hash,
        "hash": actual_hash,
    }
