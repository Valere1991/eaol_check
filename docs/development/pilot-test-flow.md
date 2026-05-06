# EAOL Pilot Test Flow — Manufacturing Margin Drop

## Objective

Test EAOL locally on a realistic enterprise case: explain why margin dropped for `Hydraulic Pump A` in April 2026.

## Business story

The enterprise expected a 28% margin on `Hydraulic Pump A`, but current margin is 17%. EAOL must correlate ERP cost deltas, supplier performance, MES incidents, QMS defects, and document context to produce probable causes and next-best actions.

## Step 1 — Start API only

```bash
cd /home/ubuntu/.openclaw/workspace/projects/eaol_check
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn apps.api.eaol_api.main:app --reload --host 0.0.0.0 --port 8000
```

Open:

- http://localhost:8000/docs
- http://localhost:8000/health

## Step 2 — Verify sector packs

```bash
curl http://localhost:8000/api/v1/sectors
```

Expected: sector packs including manufacturing/mechanical industry, finance, civil engineering, IT operations, public sector.

## Step 3 — Verify license feature

```bash
curl http://localhost:8000/api/v1/licenses/demo/features/causal_intelligence
curl http://localhost:8000/api/v1/licenses/demo/features/camunda_workflows
```

Expected: `allowed: true` for the demo tenant.

## Step 4 — Run causal analysis

```bash
curl -X POST http://localhost:8000/api/v1/causal-analysis \
  -H 'Content-Type: application/json' \
  -d @samples/pilot-manufacturing/causal_analysis_margin_drop.json
```

Expected answer:

- probable supplier cost/availability pressure
- operational bottleneck on Line 3
- QA/rework impact
- confidence scores
- evidence trace
- next-best actions including Camunda root-cause workflow

## Step 5 — Start workflow placeholder

```bash
curl -X POST http://localhost:8000/api/v1/workflows/start \
  -H 'Content-Type: application/json' \
  -d '{
    "tenant_id": "demo",
    "case_id": "pilot-margin-drop-prod-a-april-2026",
    "workflow_key": "eaol-root-cause-analysis",
    "variables": {
      "product_id": "PROD-A",
      "supplier_id": "SUP-ACME",
      "severity": "high"
    }
  }'
```

Expected: `status: accepted`.

## Step 6 — Send test notification

```bash
curl -X POST http://localhost:8000/api/v1/notifications \
  -H 'Content-Type: application/json' \
  -d '{
    "tenant_id": "demo",
    "correlation_id": "pilot-margin-drop-prod-a-april-2026",
    "channel": "in_app",
    "severity": "warning",
    "subject": "EAOL root-cause analysis completed",
    "message": "Probable cause: supplier ACME delay + Line 3 bottleneck + QA rework. Human approval required."
  }'
```

Expected: `status: queued`.

## Step 7 — Optional full infrastructure

```bash
cd infra/local
docker compose -f docker-compose.example.yml up -d postgres neo4j redpanda zeebe operate tasklist keycloak redis minio mailhog
```

Then inspect:

- Neo4j: http://localhost:7474
- Camunda Operate: http://localhost:8081
- Camunda Tasklist: http://localhost:8082
- Redpanda Console: http://localhost:8085
- Mailhog: http://localhost:8025
- MinIO: http://localhost:9001

## Pilot interpretation

This alpha does not yet ingest CSV automatically into DB/graph. For now, CSV files are test evidence and the JSON payload simulates normalized signals. The next development step is to build the CSV ingestion endpoint and project data into Postgres, Neo4j, and the event bus.
