"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an
automatic pizza order program.

Small Pizza     : $15
Medium Pizza    : $20
Large Pizza     : $25

Pepperoni for Small Pizza           : +$2
Pepperoni for Medium or Large Pizza : +$3
Extra cheese for any size pizza     : +$1 
"""

print("Welcome to Python Pizza Deliveries");
size = input("What size pizza do you want? S, M, or L ");
addPepperoni = input("Do you want Pepperoni? Y or N ");
extraCheese = input("Do you want extra cheese? Y or N ");

bill = 0;

if size == "S":
    bill += 15;
elif size == "M":
    bill += 20;
elif size == "L":
    bill += 25;

if addPepperoni == "Y":
    if size == "Y":
        bill += 2;
    else:
        bill += 3;
if extraCheese == "Y":
    bill += 1;
print(f"Your final bill is: ${bill}.");

    