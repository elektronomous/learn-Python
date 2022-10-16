from math import ceil
"""
You're painting a wall. The insructions on the paint can says that 1 can of paint can cover 5 square meter of walls.
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height X wall width) ÷ coverage per can.
e.g. height = 2, width = 4, coverage = 5

number of can   = (2 x 4) ÷ 5
                = 1.6

but because you can't buy 0,6 of a can paint, the result should be rounded up to 2 cans.

IMPORTANT: Notices the name of the function and parameters must match those on line 13 for the code
to work.
"""

def paint_calc(height, width, cover):
    cans = ceil((height * width)/cover);
    print(f"You'll need {cans} cans of paint");

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)