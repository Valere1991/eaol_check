from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apps.api.eaol_api.routers import admin, audit, auth, dashboard, imports, license, notifications, sectors, workflows

from apps.api.eaol_api.dependencies import enforce_license
from packages.eaol_core.ai.providers import get_ai_provider
from packages.eaol_core.config import settings
from packages.eaol_core.domain.models import CausalAnalysisRequest, CausalAnalysisResponse
from packages.eaol_core.licensing.models import LicenseFeature
from packages.eaol_core.reasoning.engine import HybridReasoningEngine

app = FastAPI(
    title="EAOL Check API",
    description="Enterprise AI Operating Layer — local-first alpha API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200", "http://127.0.0.1:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.env, "ai_provider": settings.ai_provider}


@app.post("/api/v1/causal-analysis", response_model=CausalAnalysisResponse)
async def causal_analysis(payload: CausalAnalysisRequest) -> CausalAnalysisResponse:
    enforce_license(payload.tenant_id, LicenseFeature.CAUSAL_INTELLIGENCE)
    engine = HybridReasoningEngine(get_ai_provider(settings.ai_provider))
    return await engine.analyze(payload)


app.include_router(license.router)
app.include_router(notifications.router)
app.include_router(sectors.router)
app.include_router(workflows.router)
app.include_router(audit.router)
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(imports.router)
app.include_router(admin.router)
