from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["dashboard"])


@router.get("/dashboard", response_class=HTMLResponse)
def dashboard() -> str:
    return """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>EAOL IT Pilot Dashboard</title>
  <style>
    body { font-family: Inter, Arial, sans-serif; margin: 32px; background: #0f172a; color: #e2e8f0; }
    .card { background: #111827; border: 1px solid #334155; border-radius: 14px; padding: 20px; margin-bottom: 16px; }
    button { background: #38bdf8; border: 0; padding: 10px 14px; border-radius: 8px; cursor: pointer; }
    pre { white-space: pre-wrap; background: #020617; padding: 16px; border-radius: 10px; }
  </style>
</head>
<body>
  <h1>EAOL IT Pilot Dashboard</h1>
  <div class="card">
    <p>Minimal local dashboard for IT-domain pilot testing. Default tenant: <strong>firma-it</strong>.</p>
    <button onclick="loadHealth()">Check Health</button>
    <button onclick="loadSectors()">Load Sectors</button>
    <button onclick="loadAudit()">Load Audit</button>
  </div>
  <pre id="out">Ready.</pre>
  <script>
    async function show(url) {
      const res = await fetch(url);
      document.getElementById('out').textContent = JSON.stringify(await res.json(), null, 2);
    }
    function loadHealth(){ show('/health'); }
    function loadSectors(){ show('/api/v1/sectors/it_operations'); }
    function loadAudit(){ show('/api/v1/audit/firma-it'); }
  </script>
</body>
</html>
"""
