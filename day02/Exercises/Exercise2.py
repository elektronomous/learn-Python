"""
EXERCISE 2 

Write a program that calculates the Body Mass Index(BMI) from
a user's weight and height.

The BMI is a messure of some's weight takint into account their
height. e.g. if a tall person and a short person both weight the same amount,
the short person is usually more overweight

the BMI is calculated by dividing a person's weight in kg by the
square of their height

BMI = weight(kg)/height**2(m**2)
"""
height = float(input("enter your height in m: "));
weight = int(input("enter your weight in kg: "));

BMI = weight/(height**2);
print(str(int(BMI)));