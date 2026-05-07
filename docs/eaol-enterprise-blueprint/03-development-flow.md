# 03 — Flow de développement complet

## Organisation produit / engineering

Équipes recommandées :

- **Product & Domain** : discovery, use cases, ROI, vertical packs.
- **Platform Backend** : APIs, tenancy, licence, audit, services cœur.
- **Data & Integration** : connecteurs, ingestion, modèles canoniques.
- **AI & Reasoning** : graph, vector, causal scoring, LLM boundary, evaluation.
- **Workflow & Automation** : BPMN, action connectors, human-in-the-loop.
- **Frontend & UX** : workbench, dashboards, explainability UI, admin.
- **Security & SRE** : IAM, Kubernetes/OKD, observability, hardening.
- **Customer Delivery** : onboarding, mapping SI, pilots, formation.

## Branching model

- `main` : production-ready, taggable.
- `develop` : intégration continue si l'équipe grandit.
- `architecture` : documents d'architecture et cadrage.
- `feature/<domain>-<topic>` : livraison feature courte.
- `release/<version>` : stabilisation release.
- `hotfix/<issue>` : corrections prod.

## Definition of Ready

Une user story n'entre pas en sprint sans :

- objectif métier clair ;
- tenant/security impact identifié ;
- données d'entrée et sortie définies ;
- contrat API ou event esquissé ;
- critères d'acceptance ;
- stratégie de test ;
- impacts conformité/audit connus.

## Definition of Done

Une story est terminée si :

- tests unitaires et intégration OK ;
- OpenAPI ou event schema à jour ;
- migration DB versionnée si nécessaire ;
- audit et tenant isolation couverts ;
- logs/metrics/traces ajoutés pour chemins critiques ;
- doc utilisateur/admin mise à jour si visible ;
- validation sécurité si données sensibles ;
- rollback ou feature flag prévu pour prod.

## Environnements

| Environnement | But | Données | Déploiement |
|---|---|---|---|
| Local | Dev rapide | mock/samples | Docker Compose optionnel |
| CI | tests automatisés | fixtures | GitHub Actions |
| Dev shared | intégration équipe | données synthétiques | Kubernetes namespace dev |
| Staging | pré-prod release | données masquées | miroir prod |
| Pilot | client pilote | données client limitées | private cloud/on-prem |
| Production | clients réels | données réelles | HA, monitoring, support |

## CI/CD cible

Voir : [eaol-development-flow.svg](./assets/eaol-development-flow.svg)

Pipeline recommandé :

1. lint + format check ;
2. tests unitaires ;
3. tests contrats API/events ;
4. SCA dépendances ;
5. SAST ;
6. build images ;
7. scan images ;
8. génération SBOM ;
9. push registry ;
10. déploiement dev ;
11. tests intégration ;
12. promotion staging ;
13. tests E2E + sécurité ;
14. validation release ;
15. déploiement prod blue/green ou canary.

## Quality gates IA

EAOL doit traiter l'IA comme un composant testable :

- dataset d'évaluation par vertical ;
- tests de non-régression sur explications ;
- mesure hallucination/claim sans preuve ;
- évaluation des scores de confiance ;
- golden traces pour incidents connus ;
- red-team prompts ;
- tests de fuite inter-tenant ;
- validation humaine sur use cases critiques.

## Release train

- Sprint de 2 semaines.
- Release interne toutes les 2 semaines.
- Release client pilot toutes les 4 semaines.
- Version enterprise stable toutes les 8 à 12 semaines après Beta.
- Versioning SemVer : `MAJOR.MINOR.PATCH`.
