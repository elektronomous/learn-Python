from turtle import Turtle, Screen
from random import randint

def main():
    # create screen where turtle object would draw with its pen
    screen = Screen();
    # create the turtle inside the screen
    turtle = Turtle();
    # change the shape of our turtle
    turtle.shape("turtle");
    # set the thickness
    turtle.pensize(5);

    # set the color mode to rgb 0 - 255
    screen.colormode(255);

    for _ in range(3, 10):
        # set the random color of the pen
        turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255));
        for n in range(0, _):
            turtle.right(360/_);
            turtle.forward(100);

    screen.exitonclick();



if __name__ == "__main__":
    main();