from dataclasses import dataclass
from typing import List

@dataclass
class Applicant:
    id: int | None
    name: str
    email: str
    phone: str
    skills: List[str]
    experience: str
    status: str = "Applied"