# EAOL Check — Enterprise AI Operating Layer

EAOL Check is a development-ready local-first foundation for an **Enterprise AI Operating Layer**: a sovereign cognitive layer above enterprise systems that explains anomalies, builds an enterprise knowledge graph, reasons over fragmented data, and orchestrates governed actions with Camunda BPMN.

## Product scope

EAOL is designed to integrate into all kinds of enterprises:

- Génie civil / construction
- Finance, banking, insurance
- IT operations / cloud / support
- Mechanical industry / manufacturing
- Public sector
- Logistics, energy, healthcare, retail, telecom, and more

## Included architecture

- FastAPI API gateway
- Hybrid reasoning engine
- Camunda 8 BPMN workflow boundary
- Kafka-compatible event backbone with Redpanda locally
- PostgreSQL + pgvector schema
- Neo4j knowledge graph seed
- Redis, MinIO, Keycloak, Mailhog local stack
- License and entitlement model
- Notification model: email, Slack, Teams, webhook, SMS, in-app
- Sector packs for finance, civil engineering, IT, manufacturing, public sector
- Security blueprint: RBAC/ABAC, tenant isolation, audit, AI provider policy

## Quick start

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
ruff check .
uvicorn apps.api.eaol_api.main:app --reload --host 0.0.0.0 --port 8000
```

Open:

- API docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## Full local infrastructure

```bash
cd infra/local
docker compose -f docker-compose.example.yml up -d
```

Local tools:

- Neo4j: http://localhost:7474
- Camunda Operate: http://localhost:8081
- Camunda Tasklist: http://localhost:8082
- Keycloak: http://localhost:8083
- Redpanda Console: http://localhost:8085
- Mailhog: http://localhost:8025
- MinIO Console: http://localhost:9001

## Example causal analysis

```bash
curl -X POST http://localhost:8000/api/v1/causal-analysis \
  -H 'Content-Type: application/json' \
  -d @samples/causal_analysis_request.json
```

## Example platform APIs

```bash
curl http://localhost:8000/api/v1/sectors
curl http://localhost:8000/api/v1/licenses/demo/features/camunda_workflows
curl -X POST http://localhost:8000/api/v1/workflows/start \
  -H 'Content-Type: application/json' \
  -d '{"tenant_id":"demo","case_id":"case-1"}'
```

## Repository structure

```text
apps/api/                 FastAPI application and routers
apps/ingestion/           Signal ingestion/event publishing boundary
apps/workers/             Camunda Zeebe workers boundary
apps/license/             License service boundary
apps/notifications/       Notification service boundary
packages/eaol_core/       Domain logic, policies, events, licensing, sectors
workflows/camunda/        BPMN process models
docs/                     Architecture, security, product, sector docs
infra/local/              Local Docker Compose stack and seed files
db/migrations/            SQL schema/migrations
samples/                  Demo payloads
tests/                    Unit and API tests
```

## Development principles

1. Local-first before DevOps.
2. Tenant isolation everywhere.
3. AI behind provider boundaries.
4. No external action without Camunda human approval.
5. Every explanation includes confidence and evidence trace.
6. Licenses and feature entitlements are first-class product objects.
