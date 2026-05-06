# Local Development Guide

## 1. Python API only

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
ruff check .
uvicorn apps.api.eaol_api.main:app --reload --port 8000
```

## 2. Full local infrastructure

```bash
cp .env.example .env
cp infra/local/docker-compose.example.yml docker-compose.yml
cd infra/local
# or run docker compose from repo root if you copy the file there
docker compose -f docker-compose.example.yml up -d
```

Local URLs:

- API: http://localhost:8000/docs
- Neo4j: http://localhost:7474
- Camunda Operate: http://localhost:8081
- Camunda Tasklist: http://localhost:8082
- Keycloak: http://localhost:8083
- Redpanda Console: http://localhost:8085
- Mailhog: http://localhost:8025
- MinIO Console: http://localhost:9001

## 3. API checks

```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/sectors
curl http://localhost:8000/api/v1/licenses/demo/features/camunda_workflows
```
