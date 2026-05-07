# 02 — Architecture entreprise cible

## Vue macro

EAOL est structuré en six plans :

1. **Experience Plane** : web app, admin UI, API, assistants métier.
2. **Integration Plane** : connecteurs, CDC, ETL, API polling, fichiers, webhooks.
3. **Knowledge Plane** : modèle canonique, graphe, index vectoriel, stockage documents.
4. **Intelligence Plane** : retrieval, causal scoring, règles, LLM, guardrails, explications.
5. **Action Plane** : workflows BPMN, validations humaines, connecteurs d'action.
6. **Trust Plane** : IAM, sécurité, audit, policy, conformité, observabilité.

Voir l'image : [eaol-target-architecture.svg](./assets/eaol-target-architecture.svg)

## Services cibles

| Domaine | Service | Responsabilité | Tech recommandée |
|---|---|---|---|
| API | API Gateway | API publique, OpenAPI, rate limits, tenant context | FastAPI / Java Spring possible |
| Identity | Auth Service | OIDC/SAML, mapping groupes, sessions | Keycloak / IdP client |
| Integration | Connector Gateway | Gestion connecteurs, credentials, sync jobs | Python workers + SDK |
| Integration | CDC / Batch Ingestion | Import CSV, SFTP, API, CDC DB, events | Kafka Connect / Debezium / custom |
| Data | Normalization Service | Mapping source vers modèle canonique EAOL | Pydantic + mapping registry |
| Data | Operational DB | tenants, licences, audits, jobs | PostgreSQL |
| Data | Vector Service | recherche sémantique docs et tickets | pgvector puis Weaviate optionnel |
| Data | Graph Service | dépendances entreprise, impacts, causal paths | Neo4j |
| Data | Object Store | documents, exports, preuves, pièces jointes | MinIO / S3 / Azure Blob |
| Intelligence | Retrieval Service | graph traversal + vector search + filters | Python |
| Intelligence | Reasoning Engine | règles, scoring, anomalies, causal inference | Python |
| Intelligence | LLM Boundary | abstraction fournisseurs IA et modèles locaux | provider adapter |
| Action | Workflow Service | BPMN, validations, SLA, escalades | Camunda / Temporal |
| Action | Action Connectors | Jira, ServiceNow, Teams, email, ERP actions | Connector SDK |
| Trust | Policy Engine | RBAC, ABAC, data access, action policy | OPA possible |
| Trust | Audit Service | journal immuable, evidence trace | PostgreSQL + WORM/SIEM |
| Ops | Observability | logs, metrics, traces, dashboards | OpenTelemetry, Prometheus, Grafana, Loki/Tempo |

## Modèle canonique EAOL

Entités minimum :

- Organization, BusinessUnit, Department, Team
- Employee, Role, Identity, Permission
- Project, Program, Task, Milestone
- Customer, Supplier, Partner
- Product, Service, Asset, Application
- Contract, Invoice, PurchaseOrder, Transaction
- Incident, Alert, Change, Problem, Risk
- Process, Workflow, Control
- Document, Evidence, KnowledgeItem
- KPI, Metric, Anomaly, Recommendation, Action

Relations minimum :

- REPORTS_TO, BELONGS_TO, OWNS, RESPONSIBLE_FOR
- DEPENDS_ON, IMPACTS, BLOCKS, CAUSES, CORRELATES_WITH
- SUPPLIES, CONSUMES, CONTRACTED_BY
- ASSIGNED_TO, PARTICIPATES_IN, APPROVES
- EVIDENCED_BY, MENTIONED_IN, SIMILAR_TO
- LOCATED_IN, GOVERNED_BY, VIOLATES, MITIGATES

## Flow de raisonnement

Voir : [data-reasoning-flow.mmd](./diagrams/data-reasoning-flow.mmd)

1. L'utilisateur pose une question ou une anomalie est détectée.
2. Policy Engine détermine les droits et le scope.
3. Retrieval Service récupère :
   - signaux structurés ;
   - chemins graphe ;
   - documents similaires ;
   - historique d'incidents ;
   - règles métier applicables.
4. Reasoning Engine calcule :
   - causes candidates ;
   - scores de confiance ;
   - impacts ;
   - incertitudes ;
   - preuves.
5. LLM Boundary synthétise uniquement dans le contexte autorisé.
6. Governance Layer vérifie les claims, sources et risques.
7. EAOL renvoie explication, preuves et actions recommandées.
8. Workflow Service orchestre validation humaine et action si approuvée.

## Multi-tenant et isolation

Trois niveaux de maturité :

1. **MVP / pilot** : tenant_id partout + séparation logique stricte.
2. **Enterprise** : namespaces Kubernetes séparés, secrets dédiés, policies dédiées.
3. **Regulated** : base dédiée par tenant, cluster dédié ou on-premise.

## Patterns d'intégration

- **Read-only pilot** : connecteurs en lecture seule, aucun write-back.
- **Guided action** : EAOL prépare l'action, humain exécute dans le système source.
- **Approved write-back** : EAOL exécute après approbation BPMN.
- **Autonomous low-risk** : uniquement pour actions à faible risque, réversibles et policy-approved.
