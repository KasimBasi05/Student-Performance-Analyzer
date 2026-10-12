"""Student Performance Analytics System - main program."""
import numpy as np
from functions import *


def line(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

df = load_data("students.csv")
line("1. DATASET OVERVIEW")
print("Columns :", list(df.columns))
print("Records :", df.shape[0])
print("\nFirst 5 records:")
print(df.head().to_string(index=False))
print("\nMissing values:", int(df.isnull().sum().sum()))

df = calculate_total_and_average(df)
df = assign_grades_and_status(df)

line("2. STUDENT RESULTS (Total, Average, Grade, Result)")
print(df[["Student_ID", "Name", "Total", "Average", "Grade", "Result"]].to_string(index=False))

line("3. CLASS STATISTICS")
best = df.loc[df["Average"].idxmax()]
worst = df.loc[df["Average"].idxmin()]
passed = int((df["Result"] == "Pass").sum())
failed = len(df) - passed
print(f"Highest average : {best['Name']} ({best['Average']})")
print(f"Lowest average  : {worst['Name']} ({worst['Average']})")
print(f"Overall class average : {np.mean(df['Average']):.2f}")
print(f"Passed : {passed}   Failed : {failed}   Pass % : {passed / len(df) * 100:.1f}%")

print("\nGrade distribution:")
print(df["Grade"].value_counts().sort_index().to_string())

line("4. SUBJECT-WISE ANALYSIS")
sub = subject_analysis(df)
print(sub.to_string(index=False))
best_sub = sub.loc[sub["Average"].idxmax()]
weak_sub = sub.loc[sub["Average"].idxmin()]
print(f"\nBest subject  : {best_sub['Subject']} (avg {best_sub['Average']})")
print(f"Weakest subject : {weak_sub['Subject']} (avg {weak_sub['Average']})")

line("5. TOP 3 PERFORMERS")
print(top_performers(df, 3).to_string(index=False))

line("6. DEPARTMENT-WISE ANALYSIS")
print(department_analysis(df).to_string())

line("7. LOW ATTENDANCE STUDENTS (< 75%)")
print(low_attendance_students(df).to_string(index=False))

df.to_csv("student_results.csv", index=False)
print("\nProcessed results saved to student_results.csv")
