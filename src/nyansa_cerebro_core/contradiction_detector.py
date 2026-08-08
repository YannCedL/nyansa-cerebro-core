from genesis_core import Evidence

def detect_contradictions(evidence_list: list) -> list:
    contradictions = []
    seen = {}
    for ev in evidence_list:
        key = (ev.get("subject"), ev.get("predicate"))
        if key in seen and seen[key] != ev.get("value"):
            contradictions.append({
                "subject": ev["subject"],
                "predicate": ev["predicate"],
                "values": [seen[key], ev["value"]]
            })
        else:
            seen[key] = ev.get("value")
    return contradictions
