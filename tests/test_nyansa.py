from nyansa_cerebro_core.orchestrator import run_investigation

def test_run_investigation():
    c = run_investigation("Airbus", ["company"])
    assert "company" in c.result["domains"]
    assert c.result["total_evidence_collected"] > 0
    assert c.confidence > 0.8

def test_partial_investigation():
    c = run_investigation("Boeing", ["company"])
    assert c.result["entity"] == "Boeing"
