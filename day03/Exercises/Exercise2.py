"""
Write a program that interpret the Body Mass Index(BMI) based on a user's
weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
+ Under 18.5 they are underweight
+ Over 18.5 but below 25 they have normal weight
+ Over 25 but below 30 they are slightly overweight
+ Over 30 but below 35 they are obese.
+ Above 35 they are clinically obese.
"""

height = float(input("enter your height in m: "));
weight = float(input("enter your height in kg: "));

bmi = round(weight/(height**2));    # // or weight/(height*height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are under weight.");
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.");
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.");
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.");
else:
    print(f"Your BMI is {bmi}, you are clinically obses.");