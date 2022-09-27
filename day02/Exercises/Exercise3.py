"""
EXERCISE 3

I was reading this article by Tim Urban - Your Life in Weeks and realised
just how little time we actually have.

https://waitbutwhy.com/2014/05/life-weeks.html

create a program using maths and f-strings that tells us how many days,
weeks, months we have left if we live until 90 years old.

it will take your current age as the input and output a message with our
time left in this format:
    You have x days, y weeks and z months left.

Where x, y and z are replaced with the actual calculated numbers

HINT
- There are 365 days in a year, 52 weeks in a year and 12 months
  in a year.
"""

age = input("What is your current age?");

ageLeft = 90 - int(age);

# how many days in your age left
days = ageLeft * 365;
# how many weeks in your age left
weeks = ageLeft * 52;
# how many months in your age left
months = ageLeft * 12;

print(f"You have {str(days)} days, {str(weeks)} weeks, and {str(months)} months left.");