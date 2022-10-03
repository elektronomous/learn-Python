# you can generate random number by importing the random module
import random

# generate random integer
print(random.randint(10, 20));

# now to generate the random float number
print(random.random());
# now how to generate a random number between 0 and 5
print(random.random() * 5);

# python list is like an array, but it can store any data type
# you have a bunch of fruits that contains
fruits = ['Apple', 'Mango', 'Orange', 'Strawberry', 'Rambutan'];
# now you want eat the first fruit
print(f"i eat my first fruit, that is an {fruits[0]}");
# the second fruit
print(f"i eat my second fruit, that is {fruits[1]}");
# now you want eat your fruit from the last fruit
print(f"i eat my last fruit, that is {fruits[-1]}");
# now you want eat from the back
print(f"i eat the two-last fruit, that is {fruits[-2]}");
# oh you forgot that you don't have Orange, but a Banana
fruits[2] = 'Banana';
# now you can enjoy the Banana
print(f"i eat the {fruits[2]}");
# your friend gives you an avocado
fruits.append('Avocado');
# oh your aunt coming from its village, and gives you a bunch of another fruits
fruits.extend(['pawpaw', 'cherry', 'Grape']);
# using list to shortcut the head and tails
headOrTail = ['Tails','Heads'];
print(headOrTail[random.randint(0,1)]);