from models.applicant import Applicant
from core.parsers import ResumeParser
from core.extractors import ResumeExtractor
from core.database import ApplicantDatabase

class ApplicantTracker:
    def __init__(self, skills_list=None):
        self.parser = ResumeParser()
        self.extractor = ResumeExtractor(skills_list)
        self.db = ApplicantDatabase()

    def process_resume(self, file_name: str, file_bytes: bytes):
        try:
            text = self.parser.parse(file_name, file_bytes)
        except ValueError as e:
            raise RuntimeError(f"Failed to process resume: {e}")

        applicant = Applicant(
            id=None,
            name=self.extractor.extract_name(text),
            email=self.extractor.extract_email(text),
            phone=self.extractor.extract_phone(text),
            skills=self.extractor.extract_skills(text),
            experience=self.extractor.extract_experience(text),
            status="Applied"
        )

        applicant.id = self.db.add_applicant(applicant)
        return applicant

    def update_status(self, applicant_id: int, status: str):
        self.db.update_status(applicant_id, status)

    def list_applicants(self):
        return self.db.get_all()

    def search_applicants(self, skill: str):
        return self.db.search_by_skill(skill)

    def close(self):
        self.db.close()