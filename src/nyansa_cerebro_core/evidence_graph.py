from typing import List, Dict, Any
from pydantic import BaseModel, Field
from genesis_core import Evidence

class InvestigationNode(BaseModel):
    entity: str
    engine_source: str
    evidence: List[Evidence] = Field(default_factory=list)
    children: List['InvestigationNode'] = Field(default_factory=list)
