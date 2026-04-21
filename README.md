# 📄 Resume Scanner

A lightweight, no-frills resume analysis tool built with pure Python and classic NLP techniques — no AI, no LLMs, just logic.

> **Personal toy project** — built to understand how ATS systems and resume parsers work under the hood.

---

## What It Does

- **Parses** PDF and DOCX resumes into clean text
- **Extracts skills** by matching against a categorized skills database
- **Scores resumes** using a simple ATS algorithm (0–100) based on sections, keywords, and length
- **Matches jobs** using TF-IDF + cosine similarity against job descriptions
- **Detects AI-written content** via heuristics — sentence variance, vocab ratio, avg length

---

## Project Structure

```
resume-scanner/
├── main.py              # Entry point
├── parser.py            # PDF / DOCX text extraction (PyMuPDF, python-docx)
├── skills.py            # Skill extraction using keyword matching
├── ats.py               # ATS scoring algorithm
├── matcher.py           # Job matching via TF-IDF + cosine similarity
├── ai_detector.py       # Heuristic AI-content detection
├── requirements.txt
└── data/
    ├── skills_database.json
    ├── job_keywords.json
    └── job_descriptions.json
```

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Run against a resume
python main.py
```

Update the file paths in `main.py` to point to your own resume samples.

---

## Tech Stack

- `PyMuPDF` — PDF parsing
- `python-docx` — DOCX parsing
- `scikit-learn` — TF-IDF vectorization & cosine similarity
- `numpy` — Heuristic scoring calculations

No transformers. No embeddings. No API calls. Just Python.

---

## Why I Built This

Wanted to understand what happens behind the scenes in ATS systems and resume parsers — before jumping to fancy ML solutions. Sometimes the best way to learn is to build the dumb version first.

---

## Limitations

- Skill matching is exact/substring-based — no semantic understanding
- ATS scoring is rule-based, not trained on real ATS data
- AI detection heuristics are rough estimates, not reliable classifiers

---

*Part of my learning projects series — [github.com/jigarbhalsod](https://github.com/jigarbhalsod)*
