# 05 — Livraison client et intégration SI

## Sous quelle forme livrer aux clients

### 1. SaaS standard

Livré comme application web + API :

- URL dédiée ;
- tenant provisionné ;
- SSO OIDC/SAML ;
- connecteurs configurés ;
- support standard ;
- SLA par plan.

### 2. Private Cloud

Livré dans le cloud ou compte du client :

- Helm chart + Terraform ;
- registry d'images ;
- documentation réseau ;
- runbooks ;
- intégration SIEM ;
- support premium.

### 3. On-Premise / OKD

Livré comme package enterprise :

- images OCI signées ;
- Helm chart compatible OKD/OpenShift ;
- valeurs d'installation ;
- procédure offline si nécessaire ;
- SBOM ;
- guide hardening ;
- guide upgrade/rollback ;
- support L2/L3.

## Phases d'onboarding client

Voir : [client-onboarding-flow.mmd](./diagrams/client-onboarding-flow.mmd)

1. **Discovery** : objectifs, use cases, sponsor, ROI attendu.
2. **SI Mapping** : ERP/CRM/ITSM/BI/GED, propriétaires, APIs, contraintes.
3. **Security Review** : IAM, données, réseau, DPA, conformité.
4. **Data Contract** : schémas source, fréquence, qualité, mappings.
5. **Pilot Read-Only** : ingestion limitée, pas d'écriture dans SI.
6. **Validation Métier** : précision, explications, temps de root cause.
7. **Action Layer** : workflows d'approbation, write-back contrôlé.
8. **Production Rollout** : HA, monitoring, support, formation.
9. **Expansion** : nouveaux domaines, connecteurs, vertical modules.

## Méthode d'intégration systèmes entreprise

### ERP

- Objets : commandes, factures, achats, stocks, centres de coûts, marges.
- Patterns : API REST/SOAP, exports batch, CDC base répliquée.
- Actions : créer tâche d'investigation, proposer correction, jamais modifier finance sans approbation.

### CRM

- Objets : comptes, opportunités, contrats, tickets client.
- Patterns : API OAuth, webhooks.
- Actions : créer follow-up, risque compte, alerte customer success.

### ITSM

- Objets : incidents, problèmes, changes, SLA, CMDB.
- Patterns : ServiceNow/Jira connectors, webhooks.
- Actions : créer incident, lier problème, recommander rollback, escalade.

### BI / Data Warehouse

- Objets : KPIs, agrégats, anomalies, rapports.
- Patterns : SQL read-only, exports, semantic layer.
- Actions : enrichir explication, pas remplacer le BI.

### HRIS

- Objets : équipes, rôles, absences, compétences.
- Patterns : API limitée, données minimisées.
- Actions : expliquer impacts organisationnels, respecter minimisation GDPR.

### GED / Documents

- Objets : contrats, procédures, comptes rendus, rapports.
- Patterns : connecteurs SharePoint, Google Drive, S3, GED métier.
- Actions : retrieval avec permissions héritées.

## Kit client à fournir

- Document d'architecture cible.
- Questionnaire SI et sécurité.
- Matrice connecteurs.
- Data mapping workbook.
- RACI projet.
- Plan pilote 6 à 8 semaines.
- Guide utilisateur.
- Guide admin.
- Guide API.
- Guide exploitation.
- Modèle DPA / sécurité.
- Plan de formation.
- Critères de go-live.

## RACI simplifié

| Activité | EAOL | Client IT | Métier | Sécurité client | Intégrateur |
|---|---|---|---|---|---|
| Discovery use case | A/R | C | A/R | C | C |
| Accès SI | C | A/R | C | A/R | R |
| Mapping données | R | R | A/R | C | R |
| Déploiement | R | A/R | I | C | R |
| Validation métier | C | C | A/R | I | C |
| Go-live | A/R | A/R | A/R | A/R | R |
| Support run | R | R | C | C | R |
