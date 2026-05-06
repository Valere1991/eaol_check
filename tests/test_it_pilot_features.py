from fastapi.testclient import TestClient

from apps.api.eaol_api.main import app


def test_it_csv_import_and_audit(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    client = TestClient(app)
    response = client.post(
        "/api/v1/imports/it/incidents?tenant_id=demo",
        files={
            "file": (
                "incidents.csv",
                "incident_id,tenant_id,opened_at,service_id,service_name,severity,status,title\n"
                "IT-1,demo,2026-05-05T08:00:00Z,SVC-PAY,Payments,critical,resolved,Latency spike\n",
                "text/csv",
            )
        },
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["rows_imported"] == 1
    assert payload["normalized_signals"][0]["type"] == "incident"

    audit = client.get("/api/v1/audit/demo")
    assert audit.status_code == 200
    assert audit.json()[0]["action"] == "it_csv_imported"


def test_german_question_returns_german_language_marker() -> None:
    client = TestClient(app)
    response = client.post(
        "/api/v1/causal-analysis",
        json={
            "tenant_id": "demo",
            "case_id": "de-case",
            "question": "Warum ist die Payments API langsamer geworden?",
            "signals": [
                {"type": "incident", "name": "Payments API latency", "value": "slow"},
            ],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["governance"]["response_language"] == "de"
    assert "Lokale KI" in data["answer"]


def test_dashboard_available() -> None:
    client = TestClient(app)
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert "EAOL IT Pilot Dashboard" in response.text
