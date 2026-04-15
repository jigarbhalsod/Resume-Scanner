import os
import json

# ---- Load JSON safely ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r") as f:
        return json.load(f)

ROLE_KEYWORDS = load_json("job_keywords.json")

# ---- DEFINE THIS (you forgot) ----
SECTIONS = ["education", "experience", "projects", "skills"]


# ---- ATS FUNCTION ----
def compute_ats(text, role="general"):
    text = text.lower()
    score = 0

    # Section scoring
    section_hits = sum(1 for sec in SECTIONS if sec in text)
    score += section_hits * 10

    # Keyword scoring
    keywords = ROLE_KEYWORDS.get(role, [])
    keyword_hits = sum(1 for kw in keywords if kw in text)
    score += keyword_hits * 5

    # Length scoring
    word_count = len(text.split())
    if 300 <= word_count <= 1000:
        score += 20
    elif word_count > 100:
        score += 10

    return min(score, 100)