# EAOL IT Domain Pilot

## Goal

Pilot EAOL on IT Operations first: Jira/ServiceNow-style incidents, changes, CMDB assets, and monitoring alerts.

## Local URLs and credentials

- EAOL API: http://localhost:8000/docs
- EAOL dashboard: http://localhost:8000/dashboard
- Camunda Zeebe gateway: `localhost:26500` with no auth in local dev
- Camunda Operate: http://localhost:8081
- Camunda Tasklist: http://localhost:8082
- Keycloak admin: http://localhost:8083 — `admin` / `admin`
- Neo4j: http://localhost:7474 — `neo4j` / `eaol-local-password`
- MinIO: http://localhost:9001 — `eaolminio` / `eaolminio123`
- Mailhog: http://localhost:8025

Note: the current Camunda local stack is intentionally development-only. Zeebe auth is disabled. If Operate/Tasklist require login in your image/version, use the Camunda local/dev auth configuration or access Zeebe through workers/API; production will use OIDC/Identity.

## Import IT CSV files with Postman

Use `POST form-data`:

- URL: `http://localhost:8000/api/v1/imports/it/incidents?tenant_id=demo`
- Body: `file` = `samples/pilot-it/incidents.csv`

Repeat with:

- `/api/v1/imports/it/changes`
- `/api/v1/imports/it/assets`
- `/api/v1/imports/it/alerts`

## Test German input / German output

```bash
curl -X POST http://localhost:8000/api/v1/causal-analysis \
  -H 'Content-Type: application/json' \
  -d @samples/pilot-it/causal_analysis_it_incident_de.json
```

Expected: `governance.response_language = de` and the synthesis text in German.

## Audit

CSV imports now create persistent local audit records in `data/eaol_audit.db`.

```bash
curl http://localhost:8000/api/v1/audit/demo
```

## Next production hardening

- Real Jira API connector with OAuth/API token
- Real ServiceNow connector
- Camunda worker deployment to Zeebe
- Keycloak realm export + JWT validation enforcement
- Postgres-backed audit instead of local SQLite fallback
- Dashboard as a real frontend app
