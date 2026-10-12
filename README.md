# 1. Project Title
**Student Performance Analytics System**

- **Name:** Kasim Baasith A
- **College / Department:** Info Institute of Engineering - B.Tech Information Technology 
- **Course:** Python with AI – EWB Courses

## 2. Objective
Teachers usually handle student marks manually, which is slow and error-prone. This project reads student data and automatically calculates totals, averages, grades, pass/fail status, subject-wise performance and top performers, so the class performance can be understood quickly.

## 3. Technologies Used
- Python 3
- NumPy (numerical calculations)
- Pandas (data loading and analysis)

## 4. Dataset Description
- File: `students.csv` (25 student records, no missing values)
- Columns: `Student_ID, Name, Department, Maths, Science, English, Computer, Tamil, Attendance`
- Departments: CSE, IT, ECE, EEE, MECH

## 5. Implementation
1. **Load data:** `pd.read_csv()` loads the CSV into a DataFrame; columns, record count and missing values are checked.
2. **Total & average:** Subject marks are converted to a NumPy array; `np.sum` and `np.mean` (axis=1) give each student's total and average.
3. **Grading rule (by average):** A+ ≥ 90, A ≥ 80, B ≥ 70, C ≥ 60, D ≥ 50, otherwise F.
4. **Pass/Fail rule:** A student passes only if marks are ≥ 40 in **every** subject (`np.all`).
5. **Loops:** A `for` loop goes through each student to assign grade and result, and another loop goes through each subject for subject-wise analysis.
6. **Analysis:** `idxmax`, `idxmin`, `nlargest`, `value_counts` and `groupby` answer questions such as highest average, best subject, pass count and department performance.
7. **Output:** Results are printed with clear headings and saved to `student_results.csv`.

## 6. Key Features
| Function (functions.py) | Purpose |
|---|---|
| `load_data()` | Reads the CSV file |
| `calculate_total_and_average()` | Total and average using NumPy |
| `get_grade()` | Applies the grading rule |
| `get_status()` | Applies the pass/fail rule |
| `assign_grades_and_status()` | Loops through students to assign grade/result |
| `subject_analysis()` | Highest, lowest, average, pass count per subject |
| `top_performers()` | Top N students by average |
| `department_analysis()` | Department-wise average and pass count |
| `low_attendance_students()` | Students with attendance below 75% |

## 7. Output / Screenshots
Run `python main.py`. Full program output:

```text
============================================================
1. DATASET OVERVIEW
============================================================
Columns : ['Student_ID', 'Name', 'Department', 'Maths', 'Science', 'English', 'Computer', 'Tamil', 'Attendance']
Records : 25

First 5 records:
Student_ID            Name Department  Maths  Science  English  Computer  Tamil  Attendance
      S001      Arun Kumar        CSE     88       92       79        95     84          94
      S002 Priya Dharshini         IT     76       81       88        90     92          91
      S003    Karthik Raja        ECE     45       52       60        48     66          72
      S004   Meena Lakshmi        CSE     92       95       90        98     89          97
      S005       Vignesh S        EEE     38       42       55        40     61          68

Missing values: 0

============================================================
2. STUDENT RESULTS (Total, Average, Grade, Result)
============================================================
Student_ID            Name  Total  Average Grade Result
      S001      Arun Kumar    438     87.6     A   Pass
      S002 Priya Dharshini    427     85.4     A   Pass
      S003    Karthik Raja    271     54.2     D   Pass
      S004   Meena Lakshmi    464     92.8    A+   Pass
      S005       Vignesh S    236     47.2     F   Fail
      S006  Naveen Kumar T    371     74.2     B   Pass
      S007       Kureshi U    293     58.6     D   Pass
      S008        Anitha R    429     85.8     A   Pass
      S009       Gokulnath    329     65.8     C   Pass
      S010     Manoj Kumar    468     93.6    A+   Pass
      S011      Harshini K    209     41.8     F   Fail
      S012      Santhosh M    399     79.8     B   Pass
      S013        Dinesh P    311     62.2     C   Pass
      S014      Nandhini V    433     86.6     A   Pass
      S015       Rahul Dev    281     56.2     D   Pass
      S016       Kavya Sri    444     88.8     A   Pass
      S017        Ashwin T    234     46.8     F   Fail
      S018   Guru Prasad E    389     77.8     B   Pass
      S019    Bala Murugan    350     70.0     B   Pass
      S020     Saravanan R    332     66.4     C   Pass
      S021         Riyas I    366     73.2     B   Pass
      S022        Gayathri    406     81.2     A   Pass
      S023         Shiva A    350     70.0     B   Pass
      S024        Aarthi T    257     51.4     D   Pass
      S025  Divya Bharathi    368     73.6     B   Pass

============================================================
3. CLASS STATISTICS
============================================================
Highest average : Manoj Kumar (93.6)
Lowest average  : Harshini K (41.8)
Overall class average : 70.84
Passed : 22   Failed : 3   Pass % : 88.0%

Grade distribution:
Grade
A     6
A+    2
B     7
C     3
D     4
F     3

============================================================
4. SUBJECT-WISE ANALYSIS
============================================================
 Subject  Highest  Lowest  Average  Passed
   Maths       97      34    67.00      23
 Science       95      39    68.84      24
 English       93      45    70.76      25
Computer       98      38    71.76      24
   Tamil       94      45    75.84      25

Best subject  : Tamil (avg 75.84)
Weakest subject : Maths (avg 67.0)

============================================================
5. TOP 3 PERFORMERS
============================================================
Student_ID          Name Department  Total  Average Grade
      S010   Manoj Kumar         IT    468     93.6    A+
      S004 Meena Lakshmi        CSE    464     92.8    A+
      S016     Kavya Sri        ECE    444     88.8     A

============================================================
6. DEPARTMENT-WISE ANALYSIS
============================================================
            Students  Avg_Marks  Passed
Department                             
CSE                7      77.97       7
ECE                5      64.92       4
EEE                3      57.27       2
IT                 6      80.67       6
MECH               4      61.20       3

============================================================
7. LOW ATTENDANCE STUDENTS (< 75%)
============================================================
Student_ID         Name  Attendance Result
      S003 Karthik Raja          72   Pass
      S005    Vignesh S          68   Fail
      S011   Harshini K          60   Fail
      S013     Dinesh P          74   Pass
      S015    Rahul Dev          70   Pass
      S017     Ashwin T          65   Fail
      S021      Riyas I          59   Pass
      S023      Shiva A          65   Pass
      S024     Aarthi T          50   Pass

Processed results saved to student_results.csv
```

## 8. Final Outcome
The system successfully analysed 25 students:
- Highest average: Manoj Kumar (93.6); lowest: Harshini K (41.8)
- Overall class average: 70.84
- 22 students passed, 3 failed (88% pass rate)
- Best subject: Tamil (75.84); weakest subject: Maths (67.0)
- Top 3 performers: Manoj Kumar, Meena Lakshmi, Kavya Sri
- Best department by average: IT (80.67)
- 9 students have attendance below 75%

## 9. Challenges & Learning
- **Challenge:** Deciding a clear pass condition. **Solution:** Defined pass as ≥ 40 in all subjects.
- **Challenge:** Deciding where to use NumPy vs Pandas. **Solution:** NumPy for calculations, Pandas for loading, filtering and grouping.
- **Learning:** Writing reusable functions, using loops with DataFrames, and organising a project for GitHub.

## 10. GitHub Repository
<PASTE YOUR GITHUB REPOSITORY LINK HERE>

---
**How to run**
```
pip install numpy pandas
python main.py
```
