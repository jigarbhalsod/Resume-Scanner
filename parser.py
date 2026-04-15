import fitz  # PyMuPDF
import docx

def parse_pdf(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return clean_text(text)

def parse_docx(path):
    doc = docx.Document(path)
    text = "\n".join([p.text for p in doc.paragraphs])
    return clean_text(text)

def clean_text(text):
    return " ".join(text.split())