# Job Applicant Tracker

An automated system to extract, store, and track applicant details from resumes with status management and search functionality. Built with Python, Streamlit, SQLite, and NLP tools.

---

## ✨ Features
- Upload resumes in PDF, TXT, or DOCX format.
- Automatically extract **Name, Email, Phone, Skills, Experience**.
- Store applicants in an SQLite database.
- Update applicant status (Applied, Shortlisted, Interviewed, Hired, Rejected).
- Search applicants by skills.
- User-friendly dashboard with Streamlit.

---

## 📂 Project Structure
```
job-applicant-tracker/
│── app.py                 # Entry point (Streamlit UI)
│── requirements.txt
│── README.md
│
├── core/
│   ├── __init__.py
│   ├── parsers.py         # Parse resumes (PDF/TXT/DOCX)
│   ├── extractors.py      # Extract Name, Email, Phone, Skills, Experience
│   ├── database.py        # Database (SQLite) operations
│   └── tracker.py         # Core logic for managing applicants
│
├── models/
│   ├── __init__.py
│   └── applicant.py       # Applicant dataclass
│
└── ui/
    ├── __init__.py
    └── app_ui.py          # Streamlit interface
```

---

## 🛠️ Requirements
- Python 3.9+ (works with Python 3.13 as well)
- pip package manager

Dependencies (from `requirements.txt`):
```
streamlit>=1.36.0
pandas>=2.0.0
PyPDF2>=3.0.0
spacy>=3.7.0
python-docx>=1.0.0
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/job-applicant-tracker.git
   cd job-applicant-tracker
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy language model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

---

## ▶️ Running the Project

Start the Streamlit app:
```bash
streamlit run app.py
```

This will open the dashboard in your browser.

---

## 📖 Usage

1. **Upload Resume** (PDF/TXT/DOCX)  
   The system extracts applicant details automatically.

2. **View Applicants**  
   See all stored applicants in a table.

3. **Update Status**  
   Change applicant status (Applied → Shortlisted → Interviewed → Hired/Rejected).

4. **Search by Skill**  
   Enter a skill (e.g., Python) to filter applicants.

---

## 🚀 Future Enhancements
- Export applicants to CSV/Excel.
- Add authentication for HR users.
- Integrate with Applicant Tracking Systems (ATS).
- Add ML model for ranking resumes.

---

## 📜 License
This project is licensed under the MIT License.