# Enterprise Knowledge Graph Model

## Core entities

```mermaid
erDiagram
    ORGANIZATION ||--o{ DEPARTMENT : contains
    DEPARTMENT ||--o{ EMPLOYEE : employs
    EMPLOYEE }o--o{ ROLE : has
    DEPARTMENT ||--o{ PROJECT : owns
    PROJECT }o--o{ PRODUCT : impacts
    CUSTOMER ||--o{ CONTRACT : signs
    SUPPLIER ||--o{ CONTRACT : supplies
    CONTRACT }o--o{ PRODUCT : covers
    ASSET }o--o{ PROCESS : supports
    INCIDENT }o--o{ PROCESS : affects
    RISK }o--o{ INCIDENT : relates_to
    TRANSACTION }o--o{ PRODUCT : concerns
    DOCUMENT }o--o{ PROJECT : documents
```

## Key relationships

- `REPORTS_TO`
- `OWNS`
- `DEPENDS_ON`
- `SUPPLIES`
- `IMPACTS`
- `PARTICIPATES_IN`
- `CAUSES`
- `BLOCKS`
- `RELATED_TO`
- `LOCATED_IN`

## Minimal Cypher seed concept

```cypher
MERGE (org:Organization {id: 'demo-org', name: 'Demo Enterprise'})
MERGE (supplier:Supplier {id: 'supplier-acme', name: 'Supplier ACME'})
MERGE (incident:Incident {id: 'incident-line-3', name: 'Production delay line 3'})
MERGE (product:Product {id: 'product-a', name: 'Product A'})
MERGE (supplier)-[:SUPPLIES]->(product)
MERGE (incident)-[:IMPACTS]->(product)
```
