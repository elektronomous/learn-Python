# create 3 print statements inside a function
def greet():
    print("hello");
    print("How are you doing man?");
    print("Nice to meet you to");

greet();

# you can create a function with its input
def greet(name):
    print(f"hello {name}");
    print(f"How do you do {name}?");
    
greet("faza");

# function with more than 1 input 
def greet(personName1, personName2):
    print(f"Hello {personName1} and {personName2}");
    print(f"How are both of you doing?");

greet("faza","akbar");

def greet(name, location):
    print(f"Hello {name}");
    print(f"What is it like {location}?");
greet("faza", "sumbawa");

# keyword argument
greet(location='Aikmel', name='Faza');