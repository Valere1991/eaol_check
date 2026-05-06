# EAOL Check — Enterprise AI Operating Layer

EAOL Check is a local-first alpha blueprint for an **Enterprise AI Operating Layer**: a cognitive layer above ERP/CRM/ITSM/BI systems that explains anomalies, maps enterprise context, and orchestrates human-in-the-loop actions through Camunda BPMN.

## What is included

- **FastAPI backend** for enterprise causal intelligence APIs
- **Hybrid reasoning engine**: graph evidence + vector/semantic context + rules + AI provider abstraction
- **Camunda BPMN workflow** for root-cause analysis and approval gates
- **Local development stack** with Postgres/pgvector, Neo4j, Kafka-compatible event bus, and Camunda Zeebe
- **Architecture docs**: blueprints, C4-style diagrams, data flow, graph model, IA integration, BPMN design
- **Mock connectors and sample data** to test locally before real enterprise integrations

## Quick start

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt

# optional local infrastructure
cp infra/local/docker-compose.example.yml docker-compose.yml
docker compose up -d postgres neo4j zeebe

# run API
uvicorn apps.api.eaol_api.main:app --reload --host 0.0.0.0 --port 8000
```

Open:

- API docs: http://localhost:8000/docs
- Health: http://localhost:8000/health

## Example API call

```bash
curl -X POST http://localhost:8000/api/v1/causal-analysis \
  -H 'Content-Type: application/json' \
  -d '{
    "tenant_id": "demo",
    "case_id": "margin-drop-q2",
    "question": "Pourquoi la marge a-t-elle chuté sur la ligne produit A ?",
    "signals": [
      {"type": "transaction", "name": "COGS", "value": 18.7, "unit": "% increase"},
      {"type": "supplier", "name": "Supplier ACME", "value": "late deliveries"},
      {"type": "incident", "name": "Production delay", "value": "line 3 bottleneck"}
    ]
  }'
```

## Repository structure

```text
apps/api/                 FastAPI application
apps/workers/             Camunda Zeebe workers
packages/eaol_core/       Domain models, reasoning, policies, providers
workflows/camunda/        BPMN process models
docs/                     Architecture, blueprints, diagrams, ADRs
infra/local/              Local-only runtime helpers
samples/                  Demo payloads and seed data
tests/                    Unit and API tests
```

## Development philosophy

1. **Local-first**: everything must be testable locally before DevOps hardening.
2. **Enterprise-grade boundaries**: multi-tenant, auditable, explainable by design.
3. **AI is a component, not the system**: deterministic policies and evidence traces wrap all AI outputs.
4. **Workflow before automation**: Camunda drives human validation before sensitive actions.
