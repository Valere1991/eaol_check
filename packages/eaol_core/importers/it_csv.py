import csv
from io import StringIO
from uuid import uuid4

from packages.eaol_core.it.models import ITImportResult


_DATASET_SIGNAL_TYPE = {
    "incidents": "incident",
    "changes": "process",
    "assets": "metric",
    "alerts": "risk",
}


def import_it_csv(
    *,
    tenant_id: str,
    dataset_type: str,
    filename: str,
    content: bytes,
) -> ITImportResult:
    text = content.decode("utf-8-sig")
    rows = list(csv.DictReader(StringIO(text)))
    signal_type = _DATASET_SIGNAL_TYPE.get(dataset_type, "document")
    normalized_signals = []
    for row in rows:
        label = (
            row.get("title")
            or row.get("service_name")
            or row.get("name")
            or row.get("metric")
            or row.get("id")
            or "IT row"
        )
        normalized_signals.append(
            {
                "type": signal_type,
                "name": label,
                "value": row,
                "source": row.get("source_system", filename),
                "confidence": 0.78,
            }
        )
    return ITImportResult(
        tenant_id=tenant_id,
        dataset_type=dataset_type,
        rows_imported=len(rows),
        source_filename=filename,
        correlation_id=f"it-import-{uuid4()}",
        normalized_signals=normalized_signals,
    )
