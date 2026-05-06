from packages.eaol_core.ai.providers import AIProvider
from packages.eaol_core.domain.models import (
    CausalAnalysisRequest,
    CausalAnalysisResponse,
    EvidenceItem,
    NextBestAction,
    ProbableCause,
)


class HybridReasoningEngine:
    """Hybrid causal reasoning: rules + graph-like evidence + AI synthesis.

    Alpha implementation is deterministic and local. Production implementation will add:
    - Neo4j graph traversal
    - pgvector semantic retrieval
    - anomaly detection models
    - policy checks and workflow orchestration
    """

    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider

    async def analyze(self, request: CausalAnalysisRequest) -> CausalAnalysisResponse:
        evidence = [
            EvidenceItem(
                source=signal.source or "local-signal",
                entity=signal.name,
                relation="RELATED_TO",
                summary=f"{signal.type}: {signal.name} = {signal.value}{' ' + signal.unit if signal.unit else ''}",
                confidence=signal.confidence,
            )
            for signal in request.signals
        ]

        has_supplier = any(s.type == "supplier" for s in request.signals)
        has_transaction = any(s.type == "transaction" for s in request.signals)
        has_incident = any(s.type == "incident" for s in request.signals)

        causes: list[ProbableCause] = []
        if has_transaction and has_supplier:
            causes.append(
                ProbableCause(
                    title="Pression fournisseur sur les coûts",
                    explanation="Les signaux combinent hausse transactionnelle et perturbation fournisseur.",
                    confidence=0.82,
                    impacted_entities=[s.name for s in request.signals if s.type in {"supplier", "transaction"}],
                    evidence=evidence,
                )
            )
        if has_incident:
            causes.append(
                ProbableCause(
                    title="Goulot opérationnel ou incident process",
                    explanation="Un incident opérationnel peut expliquer un retard, une sous-capacité ou une baisse de marge.",
                    confidence=0.74,
                    impacted_entities=[s.name for s in request.signals if s.type == "incident"],
                    evidence=evidence,
                )
            )
        if not causes:
            causes.append(
                ProbableCause(
                    title="Cause non déterminée — investigation requise",
                    explanation="Les signaux actuels sont insuffisants; collecter plus de contexte métier.",
                    confidence=0.45,
                    evidence=evidence,
                )
            )

        synthesis = await self.ai_provider.complete(request.question)
        return CausalAnalysisResponse(
            tenant_id=request.tenant_id,
            case_id=request.case_id,
            answer=synthesis,
            probable_causes=causes,
            next_best_actions=[
                NextBestAction(
                    action="Lancer le workflow Camunda Root Cause Analysis avec validation humaine",
                    owner_role="Operations Manager",
                    workflow_key="eaol-root-cause-analysis",
                    requires_human_approval=True,
                ),
                NextBestAction(
                    action="Collecter données ERP/achats/production complémentaires",
                    owner_role="Data Steward",
                    workflow_key=None,
                    requires_human_approval=False,
                ),
            ],
            governance={
                "mode": "human-in-the-loop",
                "explainability": "evidence_trace_required",
                "policy": "no_external_action_without_approval",
            },
        )
