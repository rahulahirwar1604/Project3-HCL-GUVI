import streamlit as st
import pandas as pd

from core.tracker import ApplicantTracker

class ApplicantTrackerApp:
    def __init__(self):
        st.set_page_config(page_title="Job Applicant Tracker", page_icon="📝", layout="wide")
        self.tracker = ApplicantTracker()

    def _to_dataframe(self, applicants):
        # applicants is a list of tuples (from sqlite)
        df = pd.DataFrame(applicants, columns=["ID", "Name", "Email", "Phone", "Skills", "Experience", "Status"])
        return df

    def main(self):
        st.title("📝 Job Applicant Tracker")
        st.caption("Upload resumes, auto-extract applicant details, and manage application statuses.")

        tab1, tab2, tab3 = st.tabs(["📂 Upload Resume", "📊 View Applicants", "🔍 Search by Skill"])

        # ---- Upload Resume Tab ----
        with tab1:
            st.subheader("Upload Applicant Resume")
            uploaded_file = st.file_uploader("Upload Resume (PDF/TXT)", type=["pdf", "txt"])

            if uploaded_file:
                if st.button("Process Resume"):
                    applicant = self.tracker.process_resume(uploaded_file.name, uploaded_file.read())
                    st.success(f"✅ Applicant added: {applicant.name}, Skills: {', '.join(applicant.skills)}")

        # ---- View Applicants Tab ----
        with tab2:
            st.subheader("All Applicants")
            applicants = self.tracker.list_applicants()
            if applicants:
                df = self._to_dataframe(applicants)
                st.dataframe(df, width='stretch')

                # Update applicant status
                selected_id = st.selectbox("Select Applicant ID to Update", df["ID"].tolist())
                new_status = st.selectbox("Update Status", ["Applied", "Shortlisted", "Interviewed", "Hired", "Rejected"])
                if st.button("Update Status"):
                    self.tracker.update_status(selected_id, new_status)
                    st.success(f"✅ Updated Applicant {selected_id} status to {new_status}")
            else:
                st.info("No applicants found in the database.")

        # ---- Search Tab ----
        with tab3:
            st.subheader("Search Applicants by Skill")
            skill = st.text_input("Enter skill (e.g., Python, SQL, AWS)")
            if st.button("Search"):
                results = self.tracker.search_applicants(skill)
                if results:
                    df = self._to_dataframe(results)
                    st.dataframe(df, width='stretch')
                else:
                    st.warning(f"No applicants found with skill: {skill}")