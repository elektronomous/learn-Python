"""
How to Debuggin in Python:
1. Describe the problem
"""
def my_function():
    # for i in range(1,20):
    for i in range(1, 21):
        if i == 20:
            print("You got it");
my_function();
# Notice that this function doesn't show us the "You got it value"
# You can debug with print the i variable value.
# There you go, the function range begin from 1 < 20
# Fix it by commenting out the first loop, and create the same loop

"""
2. Reproduce the bug
   = Sometimes you encounter the bug once, but you don't encounter it the next time
"""

from random import randint
dice_imgs = ["[1]", "[2]", "[3]", "[4]", "[5]", "[6]"];
# dice_num = randint(1,6);
dice_num = randint(0,5);
print(dice_imgs[dice_num]);
# When you run this code, it goes normal for a while, but occasionally
# you got an error.
# Produce the same error as the previous error you get when you run the program.
# after produce, you'll notice that the error occurs because the index is overflow
# now you figure out the error, and find how does the randint works.
# yup, you get the idea. randint will giveyou random number from 1 <= 6.
# while your list has 5 elements.
# fix the code by commenting out the problem.

"""
3. Pretending to be a computer
   = Sometimes you need to the variable inspector
"""
year = int(input("What's your year of birth"));
if year > 1980 and year < 1994:
    print("You are a millenial");
# elif year > 1994:
elif year >= 1994:
    print("You are a Gen Z");
# When you run this code, and enter 1994 it does nothing
# you can pretend to be a computer and replace the year variable
# with value you've enter.
# 
# 
#       if 1994 > 1980 and 1994 < 1994:
#           print("You are millenial")
#       elif 1994 > 1994:
#           print("You are a Gen Z");
# 
# Did you notice the error you get?
# Yup, both of the logic failed to evalute the year value
# now fix the logic by commenting out the failed logic. 

"""
4. Using IDE Red Underlines
   = Your IDE has a featuer which mark the error you create
5. Using the basic skill of programming
"""
# age = input("How old are you? ");
age = int(input("How old are you? "));
if age > 18:
# print("You can drive at age {age}.");
    # print("You can drive at age {age}.");
    print(f"You can drive at age {age}.");

# if you the red underline, that means your IDE has feature maps the error
# commenting out the red underline, and create the valid statemnets.

# after you normalize the red underline, the age give you an error again
# Because python give you a clear explanation about this error, you should be
# noticed that the age was an str data type
# so commenting out the error code, and change it to be the normal code.

# now you get the problem, the print statement doesn't show you the age value
# because you have basic skill, you'll notice that the 'f' is missing
# then you commenting out the error code and replace with the normal one

"""
6. Print is your best friend
"""

pages = 0;
word_per_page = 0;
pages = int(input("Number of pages: "));
# word_per_page == int(input("Number of words per page: "));
word_per_page = int(input("Number of word_per_page: "));
# print(f"pages: {pages}");
# print(f"word_per_page: {word_per_page}");

total_words = pages * word_per_page;
print(total_words);
# insert print statement after the word_per_page
# now you notice that the word_per_page doesn't do assignment, instead
# it does evaluate 0 with your value that you gonna input
# fix thix by commenting out, and normlize the code.

"""
7. using debugger like Thonny python or go visit the pythontutor.com
8. The last choice StackOverflow.com
"""