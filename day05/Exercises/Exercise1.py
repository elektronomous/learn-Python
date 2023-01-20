"""
You're going to write a program that calculates the average student height 
from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146];
"""

student_heights = input("Input a list of student heights? ").split();
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i]);
    
totalHeight = totalStudent = 0;

for height in student_heights:
    totalHeight += height;
    totalStudent += 1;

print(f"The average: {round(totalHeight/totalStudent)}");