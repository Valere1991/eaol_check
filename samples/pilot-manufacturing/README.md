# Pilot Manufacturing Dataset

Scenario: margin drop for `Hydraulic Pump A` in April 2026.

Expected root cause hypothesis:

1. Supplier ACME delivery degradation created missing components.
2. Missing components caused Line 3 bottleneck and overtime.
3. ACME batch quality issue increased QA defects and rework.
4. These effects explain the margin drop from 28% planned to 17% current.

Files:

- `transactions.csv`: ERP/QMS cost deltas
- `suppliers.csv`: procurement supplier risk
- `incidents.csv`: MES/QMS/ITSM incidents
- `projects.csv`: project/margin status
- `documents.csv`: document summaries for semantic context
- `causal_analysis_margin_drop.json`: ready API payload
