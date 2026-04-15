import os
import json
import re

# ---- Load JSON safely ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def load_json(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r") as f:
        return json.load(f)

SKILLS_DB = load_json("skills_database.json")


# ---- Normalization ----
def normalize(text):
    text = text.lower()
    text = text.replace("-", " ")
    text = text.replace(".", " ")
    return text


# ---- Skill Extraction ----
def extract_skills(text):
    text = normalize(text)

    found = {k: set() for k in SKILLS_DB}

    for category, skills in SKILLS_DB.items():
        for skill in skills:
            skill_norm = normalize(skill)

            if skill_norm in text:
                found[category].add(skill)

    return {k: list(v) for k, v in found.items()}