from nyansa_cerebro_core import run_investigation

def test_run_investigation():
    c = run_investigation("Airbus", ["company", "media", "geo"])
    assert "company" in c.result["results"]
    assert c.result["total_engines_used"] > 0
    assert c.confidence > 0.9

def test_partial_investigation():
    c = run_investigation("Boeing", ["company"])
    assert c.result["entity"] == "Boeing"
