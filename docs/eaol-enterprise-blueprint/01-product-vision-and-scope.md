# 01 — Vision produit et périmètre EAOL

## Positionnement

EAOL est une **couche cognitive souveraine d'entreprise** placée au-dessus des systèmes existants : ERP, CRM, HRIS, ITSM, BI, GED, MES, WMS, outils projet, outils financiers et systèmes métiers.

EAOL ne remplace pas ces systèmes. Il les rend :

- compréhensibles dans un modèle unifié ;
- corrélables entre silos ;
- explicables par preuves ;
- actionnables via workflows gouvernés ;
- auditables pour les environnements entreprise.

## Wedge product recommandé

Le premier produit vendable doit rester très clair :

> **Enterprise Causal Intelligence** : expliquer pourquoi un problème business est arrivé, avec preuves, score de confiance, impacts et prochaines actions.

Exemples :

- baisse de marge ;
- retard projet ;
- incident IT récurrent ;
- rupture fournisseur ;
- anomalie finance ;
- risque opérationnel ;
- dérive qualité ;
- surcharge d'équipe ;
- fraude potentielle.

## Promesse produit

Pour un problème métier donné, EAOL doit répondre :

1. **Ce qui se passe** : symptôme, anomalie, périmètre impacté.
2. **Pourquoi c'est probablement arrivé** : causes probables classées.
3. **Quelles preuves soutiennent l'explication** : événements, documents, tickets, transactions, relations graphe.
4. **Qui ou quoi est impacté** : équipes, clients, projets, fournisseurs, contrats, actifs.
5. **Que faire maintenant** : recommandations et actions orchestrées.
6. **Qui doit valider** : human-in-the-loop pour actions sensibles.

## Principes de design

- **Souveraineté** : SaaS, Private Cloud ou On-Premise selon la politique client.
- **Explainability-first** : aucune réponse critique sans trace de preuve.
- **Human-in-the-loop** : EAOL recommande et prépare ; l'humain approuve les actions sensibles.
- **Connector factory** : chaque intégration suit un pattern standardisé.
- **Canonical model** : les données sont normalisées avant raisonnement.
- **Graph + vector + rules + LLM** : pas de dépendance unique à un LLM.
- **Enterprise-ready** : SSO, audit, RBAC/ABAC, observabilité, HA, support et conformité.

## Produit final attendu

Un produit complet prêt PROD doit inclure :

- portail web utilisateur et admin ;
- API enterprise documentée OpenAPI ;
- connecteurs standards ;
- ingestion batch, API et event-driven ;
- knowledge graph entreprise ;
- moteur de reasoning hybride ;
- workflow d'actions gouvernées ;
- module de gouvernance IA ;
- packaging Kubernetes / OKD / Helm ;
- mode SaaS, Private Cloud et On-Prem ;
- documentation client ;
- runbooks exploitation ;
- modèle commercial clair ;
- support et onboarding partenaires intégrateurs.
