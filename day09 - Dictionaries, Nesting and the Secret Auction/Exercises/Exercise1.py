"""
You have access to a database of 'student_scores' in the format of a dictionary.
The keys in 'student_scores' are the names of the student and the values are their exam
scores.

Write a program that converts their scores to grades. By the end of your program, you should have a
new dictionary called 'student_grades' that should contain student names for keys and their grades for values.

this is the scoring criteria:
    Scores 91 - 100: Grade = "Outstanding"
    Scores 81 - 90: Grade = "Exceeds Expectations"
    Scores 71 - 80: Grade = "Acceptable"
    Scores 70 - lower: Grade = "Fail"
"""

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
};

# TODO - 1 - Create an empty dictionary called student_grades.
student_grades = {};

# TODO - 2 - Write your code below to add the grades to student_grades
for student_name in student_scores:
    score = student_scores[student_name];
    if score > 90:
        student_grades[student_name] = "Outstanding";
    elif score > 80:
        student_grades[student_name] = "Exceeds Expectations";
    elif score > 70:
        student_grades[student_name] = "Acceptable";
    else:
        student_grades[student_name] = "Fail";

print(student_grades);