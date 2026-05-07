# 07 — Plan sprint jusqu'à produit complet prêt PROD

Hypothèse : sprints de 2 semaines, produit enterprise complet en 12 à 18 mois, expansion plateforme 18 à 24 mois.

## Phase 0 — Architecture & product framing (Sprints 0 à 3)

| Sprint | Objectif | Livrables |
|---|---|---|
| S0 | Cadrage wedge | ICP, use case prioritaire, critères ROI, architecture cible |
| S1 | Modèle canonique | entités, relations, event schemas, data contracts |
| S2 | UX cible | user journeys, explainability UI, admin journeys |
| S3 | Plan delivery | backlog, risques, sécurité, plan pilote, pricing v1 |

## Phase 1 — Core Alpha (Sprints 4 à 10)

| Sprint | Objectif | Livrables |
|---|---|---|
| S4 | API foundation | tenant, auth boundary, OpenAPI, audit skeleton |
| S5 | Ingestion foundation | CSV/API ingestion, event envelope, validation |
| S6 | Canonical store | PostgreSQL model, fixtures, migrations |
| S7 | Graph foundation | Neo4j schema, dependency traversal |
| S8 | Vector foundation | pgvector docs/tickets, basic retrieval |
| S9 | Reasoning v1 | rules + causal score + evidence trace |
| S10 | Alpha pilot pack | demo métier, admin minimal, pilot docs |

## Phase 2 — Intelligence Beta (Sprints 11 à 18)

| Sprint | Objectif | Livrables |
|---|---|---|
| S11 | LLM boundary | provider abstraction, prompt policy, mock/local option |
| S12 | Evaluation suite | golden datasets, non-regression IA, claim checks |
| S13 | Explainability UI | preuves, graph paths, confidence, uncertainty |
| S14 | Connectors v1 | ITSM, ERP export, CRM export, documents |
| S15 | Anomaly detection | KPI anomaly, threshold/rules, alert events |
| S16 | Multilingual enterprise | FR/EN/DE response policy, terminology packs |
| S17 | Security beta | SSO, RBAC/ABAC, tenant leak tests |
| S18 | Beta pilot release | pilot client read-only, ROI dashboard |

## Phase 3 — Action Layer (Sprints 19 à 26)

| Sprint | Objectif | Livrables |
|---|---|---|
| S19 | BPMN foundation | Camunda/Temporal workflows, task lifecycle |
| S20 | Human approval | validation, delegation, audit action |
| S21 | Notification routing | email, Teams/Slack, webhook, escalation |
| S22 | ITSM write-back | ticket/comment/update approuvé |
| S23 | ERP/CRM guided actions | action suggestions, manual-safe mode |
| S24 | Policy engine actions | risk levels, allowed/blocked actions |
| S25 | Workflow templates | incident, margin drop, supplier risk, project delay |
| S26 | Action beta release | end-to-end explain + approve + execute |

## Phase 4 — Enterprise Hardening (Sprints 27 à 36)

| Sprint | Objectif | Livrables |
|---|---|---|
| S27 | Kubernetes packaging | Helm charts, values, ingress, secrets pattern |
| S28 | OKD/OpenShift | SCC, routes, non-root, registry docs |
| S29 | Observability | OTel, dashboards, alert rules, runbooks |
| S30 | HA & backup | Postgres/Neo4j/Kafka strategy, restore test |
| S31 | Security hardening | SAST/SCA, image scan, SBOM, signatures |
| S32 | Compliance kit | GDPR, DPA, audit exports, retention controls |
| S33 | Performance | load tests, ingestion throughput, query latency |
| S34 | Admin enterprise | tenant admin, connector admin, license admin |
| S35 | Pen test fixes | remediation security, threat model update |
| S36 | Release Candidate | PROD readiness review, go-live checklist |

## Phase 5 — Production & Scale (Sprints 37 à 48)

| Sprint | Objectif | Livrables |
|---|---|---|
| S37 | First production | controlled go-live, support hypercare |
| S38 | Support model | SLAs, incident process, customer health |
| S39 | Partner toolkit | intégrateur docs, connector SDK |
| S40 | Vertical pack 1 | IT operations / manufacturing complet |
| S41 | Vertical pack 2 | finance / insurance risk intelligence |
| S42 | Advanced analytics | portfolio risk, simulation, trend analysis |
| S43 | Marketplace connectors | packaging connecteurs certifiés |
| S44 | Advanced governance | model cards, AI policy center |
| S45 | Scale SaaS | multi-region, billing/metering, automation |
| S46 | Cost optimization | infra cost controls, model routing |
| S47 | Enterprise expansion | multi-department rollout templates |
| S48 | Platform v1.0 | produit complet enterprise-ready |

## Critères de PROD readiness

- Déploiement repeatable Kubernetes/OKD.
- SSO client validé.
- Tenant isolation prouvée.
- Backup/restore testé.
- Monitoring et alerting actifs.
- Runbooks support prêts.
- DPA/security pack prêt.
- Documentation admin/utilisateur prête.
- Incident response process défini.
- Évaluation IA stable sur datasets clients.
- Go/no-go signé par Product, Engineering, Security, Delivery.
