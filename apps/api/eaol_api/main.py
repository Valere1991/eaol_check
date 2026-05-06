from fastapi import FastAPI

from packages.eaol_core.ai.providers import get_ai_provider
from packages.eaol_core.config import settings
from packages.eaol_core.domain.models import CausalAnalysisRequest, CausalAnalysisResponse
from packages.eaol_core.reasoning.engine import HybridReasoningEngine

app = FastAPI(
    title="EAOL Check API",
    description="Enterprise AI Operating Layer — local-first alpha API",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.env, "ai_provider": settings.ai_provider}


@app.post("/api/v1/causal-analysis", response_model=CausalAnalysisResponse)
async def causal_analysis(payload: CausalAnalysisRequest) -> CausalAnalysisResponse:
    engine = HybridReasoningEngine(get_ai_provider(settings.ai_provider))
    return await engine.analyze(payload)
