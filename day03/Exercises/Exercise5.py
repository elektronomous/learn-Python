"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:

+ Take both people's name and check for the number of times the letters in the word
  TRUE occurs.
+ Then check for the number of times the letters in the word LOVE occurs.
+ Then combine theses numbers to make a 2 digit number.
"""

from http.cookiejar import LoadError


print("Welcome to the love Calculator!");

name1 = input("What is your name?\n ");
name2 = input("What is their name?\n ");

fullName = (name1 + name2).lower();

nT = fullName.count('t');
nR = fullName.count('r');
nU = fullName.count('u');
nE = fullName.count('e');
nTRUE = str(nT + nR + nU + nE);

nL = fullName.count('l');
nO = fullName.count('o');
nV = fullName.count('v');
nE = fullName.count('e');
nLOVE = str(nL + nO + nV + nE);

loveScore = int(f"{nTRUE}{nLOVE}");

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.");
elif loveScore >= 40 and loveScore < 50:
    print(f"Your score is {loveScore}, you are alright together.");
else:
    print(f"Your score is {loveScore}.");