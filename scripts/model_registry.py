"""Model registry for Innioasis and Timmkoo players."""

MODELS = [
    {"id": "Y1", "slug": "y1", "name": "Innioasis Y1", "description": "4-inch touchscreen player powered by MediaTek MT6580."},
    {"id": "Y2", "slug": "y2", "name": "Innioasis Y2", "description": "Compact button and touchscreen player powered by MediaTek MT6572 / MT6580."},
    {"id": "G1", "slug": "g1", "name": "Innioasis / Timmkoo G1", "description": "G-series MediaTek Android player."},
    {"id": "G3", "slug": "g3", "name": "Innioasis / Timmkoo G3", "description": "G-series MediaTek Android player."},
    {"id": "G5", "slug": "g5", "name": "Innioasis / Timmkoo G5", "description": "G-series MediaTek Android player."},
    {"id": "A5", "slug": "a5", "name": "Innioasis A5", "description": "A-series MediaTek player."},
    {"id": "D1", "slug": "d1", "name": "Innioasis D1", "description": "D-series MediaTek player."},
    {"id": "Q3", "slug": "q3", "name": "Innioasis / Timmkoo Q3", "description": "Q-series MediaTek Android player."},
    {"id": "Q3E", "slug": "q3e", "name": "Innioasis / Timmkoo Q3E", "description": "Q-series MediaTek player."},
    {"id": "Q5", "slug": "q5", "name": "Innioasis / Timmkoo Q5", "description": "Q-series MediaTek Android player."},
    {"id": "Q8", "slug": "q8", "name": "Innioasis / Timmkoo Q8", "description": "Q-series MediaTek player."},
    {"id": "R1", "slug": "r1", "name": "Innioasis R1", "description": "R-series MediaTek player."},
    {"id": "PR1", "slug": "pr1", "name": "Innioasis PR1", "description": "PR-series MediaTek player."},
    {"id": "SR1", "slug": "sr1", "name": "Innioasis SR1", "description": "SR-series MediaTek player."}
]

def display_name(model: dict) -> str:
    return model.get("name") or model.get("id") or ""
