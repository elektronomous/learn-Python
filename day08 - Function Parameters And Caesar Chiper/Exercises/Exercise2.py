"""
Prime numbers are numbers that can only be cleanly divided by
them selves and 1.

You need to write a function that checks whether if the number passed
in to it is prime number or not.

e.g. 2 is prime number because it's only divisible by them selves and 1.

but 4 is not prime number because it could be divisible by 1, 2, and 4.

"""

#Write your code below this line 👇
from re import L


def prime_checker(number):
    prime = [n for n in range(1,10) if not (number % n)];
    if len(prime) > 2:
        print("It's not a prime number");
    else:
        print("It's a prime number");
    print(prime);
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
