from fastapi import APIRouter, Depends, File, UploadFile

from apps.api.eaol_api.dependencies import enforce_license
from packages.eaol_core.audit.models import AuditRecord
from packages.eaol_core.audit.store import SQLiteAuditStore
from packages.eaol_core.importers.it_csv import import_it_csv
from packages.eaol_core.it.models import ITImportResult
from packages.eaol_core.licensing.models import LicenseFeature
from packages.eaol_core.security.auth import AuthPrincipal, Role, require_roles, require_tenant_access

router = APIRouter(prefix="/api/v1/imports", tags=["imports"])


@router.post("/it/{dataset_type}", response_model=ITImportResult)
async def import_it_dataset(
    dataset_type: str,
    tenant_id: str = "demo",
    file: UploadFile = File(...),
    principal: AuthPrincipal = Depends(require_roles(Role.EAOL_ADMIN, Role.CUSTOMER_ADMIN)),
) -> ITImportResult:
    require_tenant_access(tenant_id, principal)
    enforce_license(tenant_id, LicenseFeature.CSV_IMPORT)
    content = await file.read()
    result = import_it_csv(
        tenant_id=tenant_id,
        dataset_type=dataset_type,
        filename=file.filename or "upload.csv",
        content=content,
    )
    SQLiteAuditStore().append(
        AuditRecord(
            tenant_id=tenant_id,
            correlation_id=result.correlation_id,
            actor_id=principal.username,
            action="it_csv_imported",
            resource=f"it/{dataset_type}/{file.filename}",
            metadata={"rows_imported": result.rows_imported, "dataset_type": dataset_type},
        )
    )
    return result
