import io
from PyPDF2 import PdfReader
from docx import Document

class ResumeParser:
    @staticmethod
    def parse(file_name: str, file_bytes: bytes) -> str:
        if file_name.lower().endswith(".pdf"):
            reader = PdfReader(io.BytesIO(file_bytes))
            return "\n".join([page.extract_text() or "" for page in reader.pages])
        elif file_name.lower().endswith(".txt"):
            try:
                return file_bytes.decode("utf-8")
            except UnicodeDecodeError:
                return file_bytes.decode("latin-1", errors="ignore")
        elif file_name.lower().endswith(".docx"):
            doc = Document(io.BytesIO(file_bytes))
            return "\n".join([p.text for p in doc.paragraphs])
        raise ValueError(f"Unsupported file type: {file_name}")