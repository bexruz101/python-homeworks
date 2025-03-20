import csv
from collections import defaultdict

# Step 1: Create and write data to grades.csv
grades_data = [
    ["Name", "Subject", "Grade"],
    ["Alice", "Math", "85"],
    ["Bob", "Science", "78"],
    ["Carol", "Math", "92"],
    ["Dave", "History", "74"],
]

# Writing grades.csv
with open("grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(grades_data)

# Step 2: Read data from grades.csv and store in a data structure
grades = []

with open("grades.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append(
            {"Name": row["Name"], "Subject": row["Subject"], "Grade": int(row["Grade"])}
        )

# Step 3: Calculate average grades for each subject
subject_grades = defaultdict(list)

for entry in grades:
    subject_grades[entry["Subject"]].append(entry["Grade"])

average_grades = {
    subject: sum(grades) / len(grades) for subject, grades in subject_grades.items()
}

# Step 4: Write average grades to average_grades.csv
with open("average_grades.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg_grade in average_grades.items():
        writer.writerow([subject, round(avg_grade, 2)])

print("grades.csv and average_grades.csv have been successfully created.")
