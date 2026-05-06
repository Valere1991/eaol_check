# EAOL Self-Service Pilot Flow

## 1. Start infrastructure

```bash
cd infra/local
docker compose -f docker-compose.example.yml up -d
```

## 2. Start backend

```bash
cd /home/ubuntu/.openclaw/workspace/projects/eaol_check
source .venv/bin/activate
uvicorn apps.api.eaol_api.main:app --reload --host 0.0.0.0 --port 8000
```

## 3. Start Angular dashboard

```bash
cd /home/ubuntu/.openclaw/workspace/projects/eaol_check_fe
npm install --include=dev
npm start
```

Open `http://localhost:4200`.

## 4. Keycloak users

Realm: `eaol`

- EAOL admin: `admin` / `admin`
- Customer admin: `firma-admin` / `admin`
- Customer user: `firma-user` / `admin`

Current frontend shows the self-service flow and is ready for Keycloak login wiring. Backend exposes OIDC metadata at `/api/v1/auth/oidc-local`.

## 5. Admin creates a customer

```bash
curl -X POST http://localhost:8000/api/v1/admin/customers \
  -H 'Content-Type: application/json' \
  -d '{
    "tenant_id": "firma-it",
    "name": "Firma IT Pilot GmbH",
    "sector": "it_operations",
    "country": "DE",
    "admin_email": "admin@firma-it.local",
    "status": "trial"
  }'
```

## 6. Admin assigns exact license

```bash
curl -X POST http://localhost:8000/api/v1/admin/customers/firma-it/license \
  -H 'Content-Type: application/json' \
  -d '{
    "tenant_id": "firma-it",
    "customer_name": "Firma IT Pilot GmbH",
    "tier": "enterprise",
    "valid_from": "2026-05-06T00:00:00Z",
    "valid_until": "2026-06-06T23:59:00Z",
    "max_users": 75,
    "max_connectors": 6,
    "max_events_per_month": 100000,
    "features": ["causal_intelligence", "csv_import", "it_pilot", "dashboard", "notifications", "camunda_workflows"],
    "notification_channels": ["email", "teams", "slack", "webhook", "in_app", "sms"]
  }'
```

## 7. Admin creates integrations

```bash
curl -X POST http://localhost:8000/api/v1/admin/integrations \
  -H 'Content-Type: application/json' \
  -d '{
    "tenant_id": "firma-it",
    "integration_type": "jira",
    "name": "Firma Jira Cloud",
    "base_url": "https://firma-it.atlassian.net",
    "auth_mode": "api_token",
    "scopes": ["read:issues", "read:projects"],
    "config": {"project_key": "ITOPS", "api_token": "will-be-redacted"}
  }'
```

## 8. Customer imports data

```bash
curl -X POST 'http://localhost:8000/api/v1/imports/it/incidents?tenant_id=firma-it' \
  -F 'file=@samples/pilot-it/incidents.csv'
```

## 9. Customer runs analysis

```bash
curl -X POST http://localhost:8000/api/v1/causal-analysis \
  -H 'Content-Type: application/json' \
  -d @samples/pilot-it/causal_analysis_it_incident_de.json
```

Change the JSON tenant to `firma-it` for the customer pilot.

## 10. Audit

```bash
curl http://localhost:8000/api/v1/audit/firma-it
```
