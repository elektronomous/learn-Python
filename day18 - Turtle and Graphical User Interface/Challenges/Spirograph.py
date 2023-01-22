from turtle import Turtle, Screen
from random import randint

def main():
    # create a screen where the turtle would draw its pen
    screen = Screen();
    # create a turtle inside the screen
    turtle = Turtle();
    # change its shape to the turtle form
    turtle.shape("turtle");
    # set color mode to rgb 0 - 255
    screen.colormode(255)

    for _ in range(0, 355, 5):
        turtle.speed(10);
        # pick the random color
        turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255));
        turtle.left(_);
        turtle.circle(70);
        turtle.setheading(0);

    # exit when clicking the screen
    screen.exitonclick();



if __name__ == "__main__":
    main();