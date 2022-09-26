# Data Types

# String
print("Muhammad Faza Akbar"[0]);    # M
myName = "Muhammad Faza Akbar";

print(myName[0] + myName[4] + myName[5]); # Mmm
print(myName[3] + myName[6] + myName[10] + myName[12] + myName[14] + myName[17]); # aaaaAa

"""
what happens when using "123" + "456"
"""
print("123" + "456");   # 123456

# Integer
print(123 + 456);   # 579

# Float
print(1.55 + 2.3); # 3.849999

# Boleean
print(False);   # False
print(True);    # True

# Type checking using type() function
val = input("enter any value: ");
print(type(val));   # <class 'str'>

# the type() function is usefull when you doubt about your input

# String conversion using str() function
nameLength = len(input("enter your name: "));
""" 
print("you got " + nameLength + " characters on your name");    # error yow, because you can't concatenate the integer to a string

but, you can use str() function to convert the integer to string
"""
print("you have " + str(nameLength) + " characters in your name");

# Integer conversion using int()
val = int(input("try to enter non-digit value and you get the error: "));
print(type(val));   # <class 'int' >
# because you expect the integer here, you can't input a string value

# FLoat conversion using float() function

"""
EXERCISE 1

Write a program that adds the digits in a 2 digit number.
e.g if the input was 35, then the output should be 3 + 5 = 8
"""

two_digit_number = input("type a two digit number: ");
print(int(two_digit_number[0]) + int(two_digit_number[1]));


