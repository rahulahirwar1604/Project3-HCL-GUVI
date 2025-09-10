import re
import spacy

class ResumeExtractor:
    _nlp = spacy.load("en_core_web_sm")

    def __init__(self, skills_list=None):
        self.skills_list = {s.lower() for s in (skills_list or ["python","sql","aws","java","excel","tableau"])}

    def extract_name(self, text: str) -> str:
        doc = self._nlp(text)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text
        return "Unknown"

    def extract_email(self, text: str) -> str:
        match = re.search(r"[\w\.-]+@[\w\.-]+", text)
        return match.group(0) if match else "Not Found"

    def extract_phone(self, text: str) -> str:
        match = re.search(r"(?:\+?\d{1,3}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?){1,2}\d{4}", text)
        return match.group(0) if match else "Not Found"

    def extract_skills(self, text: str):
        text_lower = text.lower()
        return [s for s in self.skills_list if re.search(rf"\b{s}\b", text_lower)]

    def extract_experience(self, text: str) -> str:
        match = re.search(r"(\d+\+?)\s*(years|year|yrs)", text.lower())
        return match.group(0) if match else "Not Found"