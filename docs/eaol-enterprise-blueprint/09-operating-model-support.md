# 09 — Operating model, support et runbooks

## Operating model cible

EAOL doit être livré avec une capacité d'exploitation complète, pas uniquement du logiciel.

## Support tiers

| Niveau | Responsabilité | Exemples |
|---|---|---|
| L1 | qualification | accès utilisateur, question usage, incident simple |
| L2 | application | connecteur en erreur, workflow bloqué, job ingestion |
| L3 | engineering | bug produit, perf, sécurité, incident critique |
| Customer Success | valeur | adoption, ROI, expansion, comités pilotage |

## SLAs indicatifs

| Plan | Critique | Majeur | Standard |
|---|---:|---:|---:|
| Standard | 8h ouvrées | 1j ouvré | 3j ouvrés |
| Enterprise | 2h | 4h | 1j ouvré |
| Premium regulated | 30min-1h | 2h | 8h |

## Runbooks obligatoires

- Déploiement initial.
- Upgrade / rollback.
- Backup / restore.
- Rotation secrets.
- Incident ingestion.
- Incident connecteur.
- Incident reasoning / IA provider.
- Incident workflow.
- Incident SSO.
- Perte performance.
- Export audit client.
- Offboarding tenant.

## Customer success motion

1. Kickoff exécutif.
2. Atelier use case.
3. Atelier données.
4. Sécurité/IT review.
5. Pilot weekly steering.
6. ROI review fin pilote.
7. Plan passage production.
8. Formation champions.
9. Quarterly business review.
10. Expansion roadmap.

## Documents contractuels et techniques

- Architecture dossier.
- Security whitepaper.
- DPA.
- SLA.
- Support policy.
- Data processing inventory.
- Subprocessor list.
- Admin guide.
- User guide.
- API guide.
- Deployment guide.
- Upgrade guide.
- Release notes.
