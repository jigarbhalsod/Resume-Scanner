import numpy as np

def detect_ai(text):
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    if len(sentences) < 2:
        return 0

    lengths = [len(s.split()) for s in sentences]

    avg_len = np.mean(lengths)
    variance = np.var(lengths)

    words = text.split()
    vocab_ratio = len(set(words)) / len(words) if words else 0

    # Heuristic scoring
    score = 0

    if variance < 5:  # too uniform → AI-like
        score += 0.3

    if vocab_ratio < 0.5:
        score += 0.4

    if avg_len > 20:
        score += 0.3

    return round(min(score, 1), 3)