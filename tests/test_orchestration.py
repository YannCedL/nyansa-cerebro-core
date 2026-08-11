# test d'orchestration globale nyansa cerebro
from nyansa_cerebro_core.orchestrator import run_investigation

def test_enquete_cerebro_globale():
    contract = run_investigation("airbus", ["company"])
    assert contract is not None
    assert contract.result["entity"] == "airbus"
    assert len(contract.evidence) >= 1
    assert "company" in contract.result["domains"]
