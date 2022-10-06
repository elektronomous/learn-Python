"""
You're going to write a program that calculates the highest score
from a List of scores.

student_scores = [78, 65, 89, 86, 55];

Important: you are not allowed to use the max or min function.
"""
student_scores = [78, 65, 89, 86, 55, 91, 64, 89];
max_score = 0;

for score in student_scores:
    if(score > max_score):
        max_score = score;
print(f"the highest score in the class is: {max_score}");

    