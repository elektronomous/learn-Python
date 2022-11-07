def my_function():
    result = 3 * 2;
    return result;

"""
when you call the function

    my_function();

the function will get replace with its return statement:

    result;

now you can save the result to the variable, to make it usefull.

    output = result;

this is function result an output, where it result from the return statement

"""

""" SMALL CHALLENGE """
def format_name(f_name:str, l_name:str):
    if not f_name or not l_name:
        return "You don't specify the first and the last name.";

    return f"{f_name.lower().title()} {l_name.lower().title()}";

print(format_name("faza","akbar muhammad"));
print(format_name("","")); 