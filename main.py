from altmanai import create_receipt, emit_event, hash_artifact, verify_artifact


def main() -> None:
    payload = {"product": "DailyPilot", "action": "artifact.created"}
    expected_hash = hash_artifact(payload)

    receipt = create_receipt(
        type="artifact.created",
        actor="DailyPilot",
        summary="Generated planning artifact",
        source="python-basic-example",
    )

    event = emit_event(
        name="receipt.generated",
        source="python-basic-example",
        payload=receipt,
    )

    print({
        "receipt": receipt,
        "event": event,
        "verification": verify_artifact(payload, expected_hash),
    })


if __name__ == "__main__":
    main()
