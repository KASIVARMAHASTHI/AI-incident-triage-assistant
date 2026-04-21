from fastapi import FastAPI

from app.adapter.service import IncidentAdapter
from app.correlation.service import CorrelationEngine
from app.triage.llm_triage import LLMTriage
from app.approvals.service import ApprovalService
from app.executor.service import ExecutionEngine
from app.executor.queue import ExecutionQueue
from app.executor.retry import RetryPolicy
from app.persistence.store import IncidentStore
from app.models.contracts import IncidentRequest

app = FastAPI(title="AI Incident Triage Assistant")

adapter = IncidentAdapter()
correlation = CorrelationEngine()
triage = LLMTriage()
approval = ApprovalService()
executor = ExecutionEngine()
queue = ExecutionQueue()
retry = RetryPolicy()
store = IncidentStore()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/status/{correlation_id}")
def get_status(correlation_id: str):
    return store.get(correlation_id)

@app.post("/triage-incident")
def triage_incident(request: IncidentRequest):
    data = request.dict()
    correlation_id = data["correlation_id"]

    store.save({"correlation_id": correlation_id, "status": "received"})

    normalized = adapter.normalize(data)
    correlated = correlation.correlate(normalized)
    triage_result = triage.analyze(correlated)

    if approval.requires_approval(triage_result):
        store.save({"correlation_id": correlation_id, "status": "approval_pending"})
        return {"status": "approval_required", "triage": triage_result}

    queue.enqueue(triage_result)
    store.save({"correlation_id": correlation_id, "status": "queued"})

    return {"status": "queued", "triage": triage_result}
