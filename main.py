from parser import parse_pdf, parse_docx
from skills import extract_skills, SKILLS_DB   # ⚠️ import this also
from ats import compute_ats
from ai_detector import detect_ai
from matcher import match_jobs

def process_resume(file_path):

    # 👉 PUT IT HERE
    print("Loaded skills categories:", list(SKILLS_DB.keys()))

    if file_path.endswith(".pdf"):
        text = parse_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = parse_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

    skills = extract_skills(text)
    ats_score = compute_ats(text)
    ai_score = detect_ai(text)
    jobs = match_jobs(text)

    print("\n=== RESULTS ===")
    print("Skills:", skills)
    print("ATS Score:", ats_score)
    print("AI Probability:", ai_score)

    print("\nTop Job Matches:")
    for job, score in jobs:
        print(f"{job} → {round(score, 2)}")


if __name__ == "__main__":
    process_resume("samples/Cyber Security.pdf")
    process_resume("samples/ML_JB_3.0.pdf")