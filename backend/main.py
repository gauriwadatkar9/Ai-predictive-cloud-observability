from fastapi import FastAPI
from pydantic import BaseModel
from risk_engine import calculate_risk
from alert_engine import cluster_alerts
from ai_explainer import generate_explanation

app = FastAPI(title="AI Cloud Observability Platform")

class Metrics(BaseModel):
    cpu: float
    memory: float
    errors: int

@app.post("/analyze")
def analyze(metrics: Metrics):
    risk_score = calculate_risk(metrics.cpu, metrics.memory, metrics.errors)
    incident = cluster_alerts(metrics.cpu, metrics.memory, metrics.errors)
    explanation = generate_explanation(metrics.cpu, metrics.memory, metrics.errors)

    return {
        "risk_score": risk_score,
        "incident": incident,
        "ai_explanation": explanation
    }