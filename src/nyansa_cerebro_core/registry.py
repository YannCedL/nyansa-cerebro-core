ENGINES = {
    "company": ["argus", "ariadne", "chamber", "rosetta", "mercury"],
    "media": ["codex", "ghost", "echo", "hawk", "credence"],
    "geo": ["bedrock", "waypoint", "delta", "aquila", "nereid"],
    "platforms": ["citadel", "mirror", "terra", "mercator", "matrix", "vitals"],
    "advanced": ["raven", "beacon", "umbra", "silkroad", "odyssey", "orbit",
                 "arena", "northstar", "chronicle", "spotlight", "trail",
                 "herodotus", "kaleidoscope"],
    "support": ["gauge"]
}

def get_engines_for_query(query_type: str) -> list:
    return ENGINES.get(query_type, [])
