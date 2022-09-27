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



# Mathematical Operations
# when you add two values
print(2 + 3);       # 5
# when you substract two values
print(3 - 2);       # 1
# when you multiply two values
print(3 * 2);       # 6
# when you divide two values
print(10/5);        # 2.0
# note that when you dividing the result always a float
# you can prove it by using the type() function
print(type(10/5));  # <class 'float'>
# you can create an exponent
print(2 ** 3);      # 8

# the order of operation priority called PEMDAS from highest to lowest:
# Parentheses       => ()
# Exponent          => **
# Multiplication    => *
# Division          => /
# Addition          => +
# Substraction      => -
# you can prove it by using this example
print(3 * 3 + 3 / 3 - 3);       # my result => 7

# small challenge => using the operation above, get 3 as the result
print(3 * (3 + 3) / 3 - 3);     # 3



# how to round number instead get result like 3.999999
print(round(10/3, 2));      # 3.33
# another modifying to get rid of the number after the decimal is
# using double forward-slash(//), alternative the int converter
print(11//3);               # 3
# the type of the result is integer
print(type(11//3));         # <class 'int'>

# using the f-string to replace the formatting output
# instead of using + and the variable name
height = 1.73;
print("you height is " + str(height));  # you height is 1.73
# you can use
print(f"you height is {str(height)}");  # you height is 1.73