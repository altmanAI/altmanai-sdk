from altmanai import hash_artifact, verify_artifact


def test_verify_artifact():
    payload = {"message": "hello"}
    expected = hash_artifact(payload)
    result = verify_artifact(payload, expected)
    assert result["ok"] is True
    assert result["hash"] == expected
