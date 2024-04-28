from turtle import Turtle, Screen
import random

# first we create our turtle object
my_turtle = Turtle();

def reset():        
    # we clear the drawing turtle to go to the next challenge
    my_turtle.clear();
    # reset the position
    my_turtle.up();
    my_turtle.home();
    my_turtle.down();

def go_right(n:int):
    my_turtle.right(90);
    my_turtle.forward(n);

def go_left(n:int):
    my_turtle.left(90);
    my_turtle.forward(n);

def turn(n:int):
    my_turtle.right(180);
    my_turtle.forward(n);


def gen_random_rgb():
    r = random.randint(0, 255);
    g = random.randint(0, 255);
    b = random.randint(0, 255);

    return (r,g,b);

# we set the shape and its color
my_turtle.shape("turtle");
my_turtle.color("darkOliveGreen", "blue");

# we set the brush to be bolder
my_turtle.pensize(5);

# Challange1 - Create a rectangular
# Rectangular has 4 side which is we create 4 loops
for _ in range(4):
    my_turtle.forward(100);
    my_turtle.left(90);

reset();

# Challenge2 - Create a dashed line for about 50 paces
for _ in range(50):
    my_turtle.down();
    my_turtle.forward(3);
    my_turtle.up();
    my_turtle.forward(9);

reset();

# Challenge3 - Create a triangle, square, pentagon, hexagon, heptagon
#              octagon, nonagon and decagon
# Hint: 
# - triangle has 45° | 3 side
# - rectangular has 90° | 4 side 
# - pentagon has 72° | 5 side
# - from this we could infere that 360 / side = n°
colors = ["green", "blue", "red", "brown", "pink", "yellow"]
for side in range(3,10):
    my_turtle.pencolor(random.choice(colors));
    for n in range(0,side):
        my_turtle.right(360/side);
        my_turtle.forward(100);

reset();

# Challenge4 - Create a random move
directions = [0, 90, 180, 270];

for _ in range(100):
    my_turtle.pencolor(random.choice(colors));
    my_turtle.forward(20);
    my_turtle.setheading(random.choice(directions));

reset();

# Challenge5 - make spirograph
for degree in range(181):
    my_turtle.left(degree);
    my_turtle.pencolor(random.choice(colors));
    my_turtle.circle(50);

reset();


# we set the screen where the turtle could draw
screen = Screen();

# we only exit when we click on the screen
screen.exitonclick();