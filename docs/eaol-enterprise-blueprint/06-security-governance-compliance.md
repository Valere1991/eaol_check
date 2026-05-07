# 06 — Sécurité, gouvernance et conformité

## Objectif sécurité

EAOL traite des données stratégiques et potentiellement sensibles. Le produit doit être conçu comme une plateforme enterprise security-first dès le départ.

## Contrôles minimum PROD

- SSO OIDC/SAML.
- RBAC + ABAC.
- Tenant isolation vérifiée par tests.
- Chiffrement TLS en transit.
- Chiffrement at rest.
- Secrets via Vault/External Secrets.
- Audit immuable des accès, questions, preuves, recommandations et actions.
- SIEM integration.
- Data retention configurable.
- Export / delete GDPR.
- DPA et registre sous-traitants.
- Admin actions journalisées.
- Rate limits et anti-abuse.
- Sauvegardes testées.

## Zones de sécurité

Voir : [security-zones.mmd](./diagrams/security-zones.mmd)

1. **Public / User Zone** : navigateur, SSO, API edge.
2. **Application Zone** : API, UI, workers.
3. **Integration Zone** : connecteurs SI, gateways, credentials.
4. **Data Zone** : DB, graph, vector, object store.
5. **AI Boundary Zone** : providers externes ou modèles internes.
6. **Ops Zone** : observability, SIEM, backups.

## Gouvernance IA

Chaque réponse critique doit contenir :

- hypothèse principale ;
- causes candidates ;
- score de confiance ;
- preuves citées ;
- incertitudes ;
- données manquantes ;
- policy appliquée ;
- action recommandée ;
- besoin ou non de validation humaine.

## Compliance roadmap

| Phase | Niveau |
|---|---|
| Alpha | Secure coding, audit basique, SSO local |
| Beta | DPA, GDPR controls, tenant tests, SIEM export |
| Enterprise hardening | ISO 27001 alignment, SOC2 readiness, pen test |
| Regulated | NIS2 compatibility, on-prem hardening, offline install |

## Human-in-the-loop

Actions toujours soumises à approbation :

- modification ERP/finance ;
- modification contrat ;
- suppression données ;
- action RH sensible ;
- communication externe ;
- action IT disruptive ;
- escalade réglementaire.

Actions potentiellement automatiques si policy le permet :

- création ticket ;
- ajout commentaire interne ;
- notification équipe ;
- génération rapport ;
- enrichissement graphe ;
- classement anomalie faible risque.
