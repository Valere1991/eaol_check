# Camunda BPMN Design

## Process: `eaol-root-cause-analysis`

```mermaid
flowchart TD
    Start([Business anomaly detected]) --> Collect[Collect context]
    Collect --> Analyze[Run causal reasoning]
    Analyze --> Gateway{Confidence >= threshold?}
    Gateway -- yes --> Recommend[Generate next-best actions]
    Gateway -- no --> Steward[Data steward enrichment]
    Steward --> Analyze
    Recommend --> Approval[Human approval]
    Approval --> Approved{Approved?}
    Approved -- yes --> Execute[Execute approved action]
    Approved -- no --> CloseRejected[Close with rejected recommendation]
    Execute --> Audit[Write audit trace]
    CloseRejected --> Audit
    Audit --> End([Case closed])
```

## Worker task types

| BPMN task | Worker type | Responsibility |
|---|---|---|
| Collect context | `eaol.collect-context` | Retrieve graph/vector/source evidence |
| Run causal reasoning | `eaol.run-causal-reasoning` | Rank probable causes |
| Generate actions | `eaol.generate-actions` | Propose governed next-best actions |
| Execute action | `eaol.execute-approved-action` | Call connector only after approval |
| Audit trace | `eaol.write-audit-trace` | Persist evidence and decision trail |

## Human-in-the-loop

Sensitive automation stays blocked until a human validates:

- external system updates
- customer/supplier communication
- financial adjustment
- HR or compliance action
- high-impact operational change
