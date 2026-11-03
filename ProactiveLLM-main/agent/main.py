import os
import uvicorn
from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel

try:
    from agent.agent import run_proactive_agent
except ModuleNotFoundError:
    from agent import run_proactive_agent

app = FastAPI(
    title="Proactive Climate & Public Health Intelligence LLM API",
    description="Multi-agent health surveillance pipeline combining meteorological telemetry, hospital disease databases, and live web climate/environmental hazard intelligence (Google Search / Tavily)."
)


class AdvisoryRequest(BaseModel):
    state: str
    district: str
    city: Optional[str] = None
    language: Optional[str] = "English"


@app.post("/api/v1/proactive-advisory")
def generate_proactive_advisory(req: AdvisoryRequest):
    """Execute the 4-node proactive health pipeline for the requested location in the specified language."""
    return run_proactive_agent(state=req.state, district=req.district, city=req.city, language=req.language)


@app.get("/api/v1/proactive-advisory")
def get_proactive_advisory(
    state: str = Query(..., description="State name"),
    district: str = Query(..., description="District name"),
    city: Optional[str] = Query(None, description="City name (optional)"),
    language: Optional[str] = Query("English", description="Target response language (e.g. English, Hindi, Marathi, Bengali, Tamil, Telugu, Gujarati, etc.)")
):
    """GET endpoint to execute the 4-node proactive health pipeline in the specified language."""
    return run_proactive_agent(state=state, district=district, city=city, language=language)


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "BharatSwasthya AI - ProactiveLLM",
        "nodes": [
            "Node 1: Weather Telemetry (Open-Meteo)",
            "Node 2: Outbreak Telemetry (Hospital/Viral DB)",
            "Node 3: Natural Climate & Environmental Hazard Surveillance (ReAct Agent + Google Search/Tavily)",
            "Node 4: Multi-Hazard Proactive LLM Synthesis (Gemini Reasoner)"
        ]
    }


if __name__ == "__main__":
    app_target = "main:app" if os.path.exists("main.py") else "agent.main:app"
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    uvicorn.run(app_target, host=host, port=port, reload=True)
