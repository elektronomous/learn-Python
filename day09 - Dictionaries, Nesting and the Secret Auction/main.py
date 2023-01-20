# create a python dictionariees
from multiprocessing.sharedctypes import Value


programming_dictionaries = {
    "Bug"       : "An error in a program that prevents the program from running as expected.",
    "Function"  : "A piece of code that you can easily call over and over again."
};

# now how to retrieve python dictionaries data;
# dictionaries_name[key];
print(programming_dictionaries["Bug"]); # An error in a program that prevents the program from running as expected.

# adding items into dictionaries
# dictionaries_name[newKey] = newValue;
programming_dictionaries["Loop"] = "The action of doing something over and over again.";

# if you print out then you will get 
"""
{
    'Bug': 'An error in a program that prevents the program from running as expected.', 
    'Function': 'A piece of code that you can easily call over and over again.', 
    'Loop': 'The action of doing something over and over again.'
}
"""
# create empty|wipe out the dictionary
# programming_dictionaries = {}
empty_dictionary = {}

# you can also redefine the value of a key in dictionary
programming_dictionaries["Bug"] = "A moth in your computer.";

# now you can loop through the dictionary
for thing in programming_dictionaries:
    print(thing);
# the thing is only the key, now to fetch its value you index the dictionaries using each of the key
for key in programming_dictionaries:
    print(programming_dictionaries[key]);
