from .registry import get_engines_for_query

def plan_investigation(entity: str, query_types: list) -> dict:
    plan = {"entity": entity, "steps": []}
    for qt in query_types:
        engines = get_engines_for_query(qt)
        plan["steps"].append({"type": qt, "engines": engines, "parallel": True})
    return plan

# timeout handling added for slow engines
