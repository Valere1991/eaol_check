from fastapi.testclient import TestClient

from apps.api.eaol_api.main import app


def test_firma_it_license_is_active() -> None:
    client = TestClient(app)
    response = client.get("/api/v1/licenses/firma-it/features/causal_intelligence")
    assert response.status_code == 200
    data = response.json()
    assert data["allowed"] is True
    assert data["tenant_id"] == "firma-it"
    assert data["status"] == "active"


def test_expired_license_blocks_protected_capability_and_notifies_all_channels() -> None:
    client = TestClient(app)
    response = client.post(
        "/api/v1/causal-analysis",
        json={
            "tenant_id": "expired-it",
            "case_id": "expired-case",
            "question": "Why is the service down?",
            "signals": [{"type": "incident", "name": "outage", "value": "down"}],
        },
    )
    assert response.status_code == 402
    detail = response.json()["detail"]
    assert detail["status"] == "expired"
    assert set(detail["notifications_queued_for_channels"]) == {
        "email",
        "teams",
        "slack",
        "webhook",
        "in_app",
        "sms",
    }
