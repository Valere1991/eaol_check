# ADR 0001 — Local-first Python + Camunda architecture

## Status
Accepted

## Context
EAOL needs rapid local testing, AI integration flexibility, graph/vector reasoning, and BPMN orchestration.

## Decision
Use a Python monorepo for the alpha:

- FastAPI for APIs
- Python package for domain/reasoning/policies
- Camunda 8 BPMN/Zeebe for workflow orchestration
- Neo4j and pgvector as target persistence layers
- Mock AI provider by default

## Consequences
Positive:

- Fast iteration for AI and data reasoning
- Simple local tests
- Clear path to enterprise BPMN

Tradeoffs:

- Camunda worker integration needs hardening later
- High-scale ingestion may need JVM/Go services in later phases
