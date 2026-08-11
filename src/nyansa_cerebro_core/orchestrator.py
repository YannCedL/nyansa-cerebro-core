# orchestrateur central nyansa cerebro combinant les plateformes d'investigation

from datetime import datetime, timezone
from genesis_core import ResultContract, Evidence, EpistemicStatus, Claim, verifier_contradictions
from citadel_company_platform.engine import company_full_profile
from .planner import plan_investigation

def run_investigation(entity: str, query_types: list = None) -> ResultContract:
    # lance une enquete complete multi-domaines sur une entite (entreprise, personne, lieu)
    now_iso = datetime.now(timezone.utc).isoformat()
    contract = ResultContract(engine_version="1.0.0", observed_at=now_iso)
    
    if query_types is None:
        query_types = ["company", "geo"]
        
    plan = plan_investigation(entity, query_types)
    domain_results = {}
    all_claims = []
    
    # 1. Enquête Corporate via CITADEL si demandé
    if "company" in query_types:
        citadel_res = company_full_profile(entity)
        domain_results["company"] = citadel_res.result
        
        # conversion des preuves en claims pour la detection de contradictions
        for ev in citadel_res.evidence:
            contract.add_evidence(ev)
            all_claims.append(Claim(
                claim_id=f"claim_{len(all_claims)+1}",
                subject=ev.subject,
                predicate=ev.predicate,
                value=str(ev.value),
                source=ev.source,
                timestamp=ev.observed_at,
                confidence=ev.confidence,
                status=ev.status
            ))

    # 2. Détection automatique des contradictions croisées
    contradictions = verifier_contradictions(all_claims)
    contras_dump = [c.model_dump() for c in contradictions]

    contract.result = {
        "entity": entity,
        "query_types": query_types,
        "plan": plan,
        "domains": domain_results,
        "contradictions_detected": contras_dump,
        "total_evidence_collected": len(contract.evidence),
        "status": "investigation_terminee"
    }
    
    contract.add_evidence(Evidence(
        subject=entity,
        predicate="synthese_cerebro",
        value=f"Enquête terminée sur {len(domain_results)} domaines ({len(contradictions)} contradictions)",
        source="nyansa_cerebro_core",
        observed_at=now_iso,
        confidence=0.96,
        status=EpistemicStatus.FACT
    ))
    
    return contract
