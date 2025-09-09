from core.tracker import ApplicantTracker

def main():
    tracker = ApplicantTracker()

    print("=== Job Applicant Tracker ===")

    # Example usage (replace with resume file uploads in production)
    with open("sample_resume.txt", "rb") as f:
        applicant = tracker.process_resume("sample_resume.txt", f.read())
        print("Applicant Added:", applicant)

    print("\nAll Applicants in Database:")
    for row in tracker.list_applicants():
        print(row)

if __name__ == "__main__":
    main()