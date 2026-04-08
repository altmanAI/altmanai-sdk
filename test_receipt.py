from altmanai import create_receipt


def test_create_receipt():
    receipt = create_receipt(
        type="artifact.created",
        actor="DailyPilot",
        summary="Created planning artifact",
        source="dailypilot-engine",
        timestamp="2026-04-08T00:00:00Z",
    )
    assert receipt.type == "artifact.created"
    assert receipt.hash
    assert receipt.id.startswith("receipt_")
