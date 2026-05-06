from fastapi.testclient import TestClient

from apps.api.eaol_api.main import app


def test_health() -> None:
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_causal_analysis() -> None:
    client = TestClient(app)
    response = client.post(
        "/api/v1/causal-analysis",
        json={
            "tenant_id": "demo",
            "case_id": "case-1",
            "question": "Pourquoi la marge baisse ?",
            "signals": [
                {"type": "transaction", "name": "COGS", "value": 12.5, "unit": "%"},
                {"type": "supplier", "name": "ACME", "value": "late deliveries"},
            ],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["case_id"] == "case-1"
    assert data["probable_causes"]
