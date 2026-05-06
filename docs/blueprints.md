# EAOL Blueprints

## Blueprint 1 — Enterprise Causal Intelligence

**Goal:** explain why a business anomaly happened.

### Flow

```mermaid
sequenceDiagram
    participant User
    participant API as EAOL API
    participant Policy as Policy Layer
    participant Graph as Knowledge Graph
    participant Vector as Vector Store
    participant Reasoning as Reasoning Engine
    participant AI as AI Provider
    participant Camunda

    User->>API: Ask root-cause question
    API->>Policy: Check tenant, role, purpose
    Policy->>Graph: Fetch related entities/dependencies
    Policy->>Vector: Retrieve semantic context/documents
    Graph-->>Reasoning: Entity paths + impact links
    Vector-->>Reasoning: Relevant context chunks
    Reasoning->>AI: Bounded synthesis prompt
    AI-->>Reasoning: Explanation draft
    Reasoning-->>API: Causes + confidence + evidence
    API->>Camunda: Start approval workflow if action needed
    API-->>User: Explainable answer + next-best actions
```

### Output contract

- Probable causes ranked by confidence
- Evidence trace for every claim
- Impacted entities and dependencies
- Recommended actions
- Human approval requirement before execution

## Blueprint 2 — Connector Factory

```mermaid
flowchart TD
    S[Source System] --> C[Connector Adapter]
    C --> V[Validation]
    V --> M[Canonical Mapping]
    M --> E[Event Envelope]
    E --> K[Event Bus]
    K --> G[Graph Projection]
    K --> X[Vector Projection]
    K --> A[Audit Projection]
```

Connector categories:

- API pull connectors
- Webhook/event connectors
- Batch import connectors
- CDC connectors
- Document ingestion connectors

## Blueprint 3 — Governed AI Integration

```mermaid
flowchart LR
    Q[User Question] --> P[Policy Check]
    P --> R[Retrieval Plan]
    R --> G[Graph Retrieval]
    R --> V[Vector Retrieval]
    G --> B[Bounded Prompt Builder]
    V --> B
    B --> L[LLM Provider]
    L --> C[Claim Checker]
    C --> E[Evidence Trace]
    E --> O[Final Answer]
```

Rules:

1. No LLM answer without evidence references.
2. No external action without Camunda approval.
3. AI provider is swappable: mock, OpenAI, Azure OpenAI, Mistral, local LLM.
4. Tenant data never crosses provider boundary unless policy allows it.
