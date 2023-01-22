from turtle import Turtle, Screen
from random import choice, randint

def main():
    # create a screen where turtle would draw with its pen
    screen = Screen();
    # create the turtle object
    turtle = Turtle();
    # change its shape to a real turtle
    turtle.shape("turtle");
    # change the mode of the pen color so we can use rgb 0 - 255 mode
    screen.colormode(255);
    # make the pen thick
    turtle.pensize(5);

    for _ in range(100):
        # each time we draw a line, we pick random color
        turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255));
        turtle.setheading(choice([0, 90, 180, 270]));
        turtle.forward(10);
    
    # exit when click the screen
    screen.exitonclick();

if __name__ == "__main__":
    main();