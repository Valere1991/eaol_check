# 04 — Déploiement Kubernetes, OKD et on-premise

## Modes de déploiement

| Mode | Client cible | Hébergement | Isolation | Avantage |
|---|---|---|---|---|
| SaaS multi-tenant | SMB / mid-market | cloud EAOL | logique + namespaces | coût bas, onboarding rapide |
| SaaS single-tenant | mid-market / enterprise | cloud EAOL dédié | cluster ou namespace dédié | compromis sécurité/coût |
| Private Cloud | enterprise | cloud client | compte/subscription client | conformité interne |
| On-Premise / OKD | regulated / souverain | datacenter client | cluster client | contrôle maximal |

## Architecture Kubernetes cible

Voir : [eaol-kubernetes-okd.svg](./assets/eaol-kubernetes-okd.svg)

Namespaces recommandés :

- `eaol-system` : operators, ingress, cert-manager, policies.
- `eaol-prod` : workloads application.
- `eaol-data` : services data si non managés.
- `eaol-observability` : Prometheus, Grafana, Loki, Tempo.
- `eaol-security` : Vault/External Secrets, OPA/Gatekeeper.

## Workloads

- `api-gateway` : stateless, HPA.
- `admin-ui` / `web-ui` : stateless.
- `ingestion-workers` : autoscaling sur lag Kafka.
- `reasoning-service` : CPU/RAM scalable, GPU optionnel selon modèle.
- `workflow-workers` : stateless, idempotents.
- `connector-workers` : isolables par connecteur et tenant.
- `notification-service` : stateless avec retry queue.
- `audit-service` : stateless, écritures append-only.

## Data layer

Options :

1. **Managed preferred** : PostgreSQL managé, Neo4j Aura/Enterprise, object store cloud, Kafka managé.
2. **Self-hosted Kubernetes** : operators PostgreSQL, Neo4j, Kafka/Strimzi, MinIO.
3. **On-prem strict** : stockage client, backup client, réseau client, registry client.

Pour OKD/OpenShift :

- Routes OpenShift ou Ingress Controller ;
- SecurityContextConstraints adaptées ;
- images non-root ;
- registry interne ;
- sealed secrets / External Secrets ;
- NetworkPolicies strictes ;
- GitOps via Argo CD ou OpenShift GitOps.

## Packaging livré

Livrables infra :

- Helm chart `eaol-platform` ;
- Helm values par mode : `values-saas.yaml`, `values-private-cloud.yaml`, `values-okd.yaml` ;
- Kustomize overlays optionnels ;
- Terraform modules cloud ;
- manifests NetworkPolicy ;
- dashboards Grafana ;
- alert rules Prometheus ;
- runbooks exploitation ;
- backup/restore procedures ;
- upgrade guide.

## Sécurité déploiement

- TLS partout.
- Secrets hors Git.
- mTLS service mesh optionnel pour enterprise.
- Images signées Cosign.
- SBOM CycloneDX/SPDX.
- Admission policy : pas de root, pas de privileged, ressources obligatoires.
- NetworkPolicy deny-by-default.
- Audit Kubernetes activé.
- Logs vers SIEM client.

## Stratégie rollout

- Dev : rolling update.
- Staging : blue/green.
- Prod SaaS : canary progressif.
- Prod client privé : blue/green ou maintenance window.
- On-prem : package versionné + rollback chart + backup préalable.
