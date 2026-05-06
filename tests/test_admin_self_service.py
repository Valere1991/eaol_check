from fastapi.testclient import TestClient

from apps.api.eaol_api.main import app


def test_admin_customer_license_integration_flow(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    client = TestClient(app)

    customer = client.post(
        "/api/v1/admin/customers",
        json={
            "tenant_id": "acme-it",
            "name": "ACME IT",
            "sector": "it_operations",
            "country": "DE",
            "admin_email": "admin@acme.local",
            "status": "trial",
        },
    )
    assert customer.status_code == 200
    assert customer.json()["tenant_id"] == "acme-it"

    license_response = client.post(
        "/api/v1/admin/customers/acme-it/license",
        json={
            "tenant_id": "ignored",
            "customer_name": "ACME IT",
            "tier": "enterprise",
            "valid_from": "2026-05-06T00:00:00Z",
            "valid_until": "2026-06-06T23:59:00Z",
            "max_users": 50,
            "max_connectors": 5,
            "max_events_per_month": 10000,
            "features": ["causal_intelligence", "csv_import", "camunda_workflows"],
            "notification_channels": ["email", "teams", "slack", "webhook", "in_app", "sms"],
        },
    )
    assert license_response.status_code == 200
    assert license_response.json()["tenant_id"] == "acme-it"

    integration = client.post(
        "/api/v1/admin/integrations",
        json={
            "tenant_id": "acme-it",
            "integration_type": "jira",
            "name": "ACME Jira",
            "base_url": "https://acme.atlassian.net",
            "auth_mode": "api_token",
            "scopes": ["read:issues"],
            "config": {"api_token": "secret", "project_key": "IT"},
        },
    )
    assert integration.status_code == 200
    assert integration.json()["config"]["api_token"] == "***redacted***"

    audit = client.get("/api/v1/audit/acme-it")
    assert audit.status_code == 200
    assert {row["action"] for row in audit.json()} >= {
        "customer_created",
        "license_assigned",
        "integration_created",
    }
