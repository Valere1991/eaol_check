# Licensing and Commercial Model

## License tiers

| Tier | Target | Features |
|---|---|---|
| Starter | SMB pilot | causal intelligence, limited users, limited connectors |
| Professional | Mid-market | graph, vector search, Camunda workflows, standard connectors |
| Enterprise | Large enterprise | advanced connectors, sector packs, SIEM export, higher limits |
| Sovereign | Regulated/on-prem | custom AI provider, on-prem, white-label, offline license validation |

## Metered dimensions

- Active users
- Connectors enabled
- Events per month
- Documents indexed
- Workflow instances
- AI tokens/requests
- Sector packs enabled
- Environments: dev/test/prod

## License enforcement points

- API middleware before feature access
- Connector activation
- Workflow start
- AI provider calls
- SIEM/export activation
- Tenant administration

## Offline/on-prem licensing

Sovereign deployments need signed license files with:

- customer identifier
- validity period
- feature entitlements
- usage limits
- signature and key version
- grace period policy

The alpha includes domain models and a feature check service; signed license validation can be added without changing API contracts.
