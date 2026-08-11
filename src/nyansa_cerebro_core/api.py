from fastapi import FastAPI
from typing import List, Optional
from genesis_core import ResultContract
from .orchestrator import run_investigation

app = FastAPI(
    title="NYANSA Intelligence Orchestrator API",
    description="Central OSINT Intelligence Platform — Autonomous Multi-Engine Investigation",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "ok", "engine": "NYANSA", "version": "1.0.0", "engines_total": 36}

@app.get("/api/v1/investigate", response_model=ResultContract)
def investigate(entity: str, query_types: Optional[str] = "company,media,geo"):
    types = [t.strip() for t in query_types.split(",")]
    return run_investigation(entity, types)
