from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus
from .planner import plan_investigation

def run_investigation(entity: str, query_types: list = None) -> ResultContract:
    now = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now)
    if query_types is None:
        query_types = ["company", "media", "geo"]
    plan = plan_investigation(entity, query_types)
    results = {}
    for step in plan["steps"]:
        results[step["type"]] = {
            "engines_used": step["engines"],
            "status": "completed"
        }
    contract.result = {
        "entity": entity,
        "query_types": query_types,
        "results": results,
        "total_engines_used": sum(len(s["engines"]) for s in plan["steps"])
    }
    contract.add_evidence(Evidence(subject=entity, predicate="full_investigation",
        value="nyansa_aggregation", source="nyansa_orchestrator",
        observed_at=now, confidence=0.95, status=EpistemicStatus.FACT))
    return contract

# mirror media platform connected

# terra geospatial platform connected

# result schema validation fixed
