"""Reusable functions for the Student Performance Analytics System."""
import numpy as np
import pandas as pd

SUBJECTS = ["Maths", "Science", "English", "Computer", "Tamil"]
PASS_MARK = 40          # minimum marks needed in EVERY subject to pass
MIN_ATTENDANCE = 75     # attendance % below this is flagged


def load_data(file_path):
    """Read the student CSV into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total_and_average(df):
    """Add Total and Average columns using NumPy."""
    marks = df[SUBJECTS].to_numpy()                 # DataFrame -> NumPy array
    df["Total"] = np.sum(marks, axis=1)             # row-wise total
    df["Average"] = np.round(np.mean(marks, axis=1), 2)
    return df


def get_grade(average):
    """Grading rule based on average marks."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def get_status(marks):
    """Pass only if the student scores >= PASS_MARK in all subjects."""
    return "Pass" if np.all(np.array(marks) >= PASS_MARK) else "Fail"


def assign_grades_and_status(df):
    """Loop through every student and assign Grade and Result."""
    grades, results = [], []
    for _, row in df.iterrows():                    # loop over each student
        grades.append(get_grade(row["Average"]))
        results.append(get_status(row[SUBJECTS].values))
    df["Grade"] = grades
    df["Result"] = results
    return df


def subject_analysis(df):
    """Highest, lowest, average and pass count for each subject."""
    rows = []
    for subject in SUBJECTS:                        # loop over each subject
        col = df[subject].to_numpy()
        rows.append({
            "Subject": subject,
            "Highest": np.max(col),
            "Lowest": np.min(col),
            "Average": round(float(np.mean(col)), 2),
            "Passed": int(np.sum(col >= PASS_MARK)),
        })
    return pd.DataFrame(rows)


def top_performers(df, n=3):
    """Return top n students by average marks."""
    return df.nlargest(n, "Average")[["Student_ID", "Name", "Department", "Total", "Average", "Grade"]]


def department_analysis(df):
    """Average marks and pass count per department (Pandas groupby)."""
    return df.groupby("Department").agg(
        Students=("Student_ID", "count"),
        Avg_Marks=("Average", "mean"),
        Passed=("Result", lambda r: (r == "Pass").sum()),
    ).round(2)


def low_attendance_students(df):
    """Students whose attendance is below the minimum."""
    return df[df["Attendance"] < MIN_ATTENDANCE][["Student_ID", "Name", "Attendance", "Result"]]
