import sqlite3
from models.applicant import Applicant

class ApplicantDatabase:
    def __init__(self, db_name="applicants.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS applicants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            experience TEXT,
            status TEXT
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def add_applicant(self, applicant: Applicant):
        query = "INSERT INTO applicants (name,email,phone,skills,experience,status) VALUES (?,?,?,?,?,?)"
        cur = self.conn.execute(query, (
            applicant.name,
            applicant.email,
            applicant.phone,
            ", ".join(applicant.skills),
            applicant.experience,
            applicant.status
        ))
        self.conn.commit()
        return cur.lastrowid

    def update_status(self, applicant_id: int, status: str):
        query = "UPDATE applicants SET status=? WHERE id=?"
        self.conn.execute(query, (status, applicant_id))
        self.conn.commit()

    def get_all(self):
        cur = self.conn.execute("SELECT * FROM applicants")
        return cur.fetchall()

    def search_by_skill(self, skill: str):
        cur = self.conn.execute("SELECT * FROM applicants WHERE LOWER(skills) LIKE ?", (f"%{skill.lower()}%",))
        return cur.fetchall()

    def close(self):
        self.conn.close()