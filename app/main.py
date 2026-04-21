from fastapi import FastAPI

app = FastAPI(title="AI Incident Triage Assistant")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/triage-incident")
def triage_incident(payload: dict):
    return {
        "message": "Incident received",
        "next": "Adapter -> Correlation -> Triage -> Approval"
    }