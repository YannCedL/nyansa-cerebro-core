import os
from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from typing import List, Optional
from genesis_core import ResultContract
from .orchestrator import run_investigation

app = FastAPI(
    title="NYANSA Cerebro Core API",
    description="Orchestrateur Central d'Intelligence OSINT & Fusion d'Évidences",
    version="1.0.0"
)

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates", "index.html")

@app.get("/", response_class=HTMLResponse)
def index():
    # sert la page d'accueil du centre de commande cerebro
    if os.path.exists(TEMPLATE_PATH):
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>NYANSA Cerebro API - Dashboard non trouve</h1>"

@app.get("/health")
def health():
    return {"status": "ok", "core": "Cerebro", "version": "1.0.0"}

@app.get("/api/v1/investigate", response_model=ResultContract)
def investigate(entity: str = Query(..., description="Sujet d'investigation"), query_types: Optional[str] = "company,media,geo"):
    types = [t.strip() for t in query_types.split(",")]
    return run_investigation(entity, types)
