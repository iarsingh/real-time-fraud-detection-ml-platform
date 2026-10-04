from fastapi.testclient import TestClient
from rtfraud.main import app

client = TestClient(app)


def test_high_and_low():
    assert client.post("/score", json={'amount': 2000, 'device_changes': 3, 'merchant_risk': 1}).json()["label"]
    high = client.post("/score", json={'amount': 2000, 'device_changes': 3, 'merchant_risk': 1}).json()
    low = client.post("/score", json={'amount': 8, 'device_changes': 0, 'merchant_risk': 0}).json()
    assert high["label"] != low["label"]
    assert high["score"] > low["score"]


def test_missing_is_refused():
    body = dict({'amount': 2000, 'device_changes': 3, 'merchant_risk': 1})
    body.pop("amount")
    assert client.post("/score", json=body).status_code == 422
