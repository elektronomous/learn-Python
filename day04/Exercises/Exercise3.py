"""
You are going to write a program that will mak a spot with an 'X'.
['🔳','🔳','🔳']
['🔳','🔳','🔳']
['🔳','🔳','🔳']

your job is to write a program that allows you to mark a square on the map using
two-digit system. the first digit is the vertical location and the second digit
is the horizontal location. so an input of 23 should place an 'X' at the position
show below:

['🔳','🔳','🔳']
['🔳','🔳','🔳']
['🔳','X','🔳']

"""

from turtle import position


row1 = ['🔳','🔳','🔳'];
row2 = ['🔳','🔳','🔳'];
row3 = ['🔳','🔳','🔳'];

ourMap = [row1, row2, row3];

position = input("Where you do you want to put the treasure? ");

if len(position) == 2:
    column = int(position[0]);
    row = int(position[1]);
    
    if row == 0:
        row = 1;
    if column == 0:
        column = 1;
    
    if row <= len(ourMap) and column <= len(row1):
        ourMap[row-1][column-1] = 'X';

print(f"{row1}\n{row2}\n{row3}");