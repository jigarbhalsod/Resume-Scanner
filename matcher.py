import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---- Load JSON safely ----
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

with open(os.path.join(DATA_DIR, "job_descriptions.json")) as f:
    JOBS = json.load(f)


# ---- PREPROCESS FUNCTION (PUT HERE) ----
def preprocess(text):
    return text.lower()


# ---- MAIN MATCH FUNCTION ----
def match_jobs(resume_text, top_k=3):
    job_texts = [job["description"] for job in JOBS]

    # Apply preprocessing HERE
    docs = [preprocess(resume_text)] + [preprocess(j) for j in job_texts]

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(docs)

    scores = cosine_similarity(vectors[0:1], vectors[1:])[0]

    results = [
        (JOBS[i]["role"], round(scores[i], 3))
        for i in range(len(scores))
    ]

    results.sort(key=lambda x: x[1], reverse=True)

    return results[:top_k]