from turtle import Turtle, Screen
from random import randint

def main():
    # create a screen where our turtle would draw
    screen = Screen();
    # create a turtle object inside the screen
    turtle = Turtle();
    # change its shape to a turtle
    turtle.shape("turtle");
    # we set the color mode to using rgb from 0 - 255
    screen.colormode(255);
    # we set the thickness of the pen
    turtle.pensize(7);

    turtle.penup();
    turtle.goto(-300, 0);

    for _ in range(50):
        turtle.pendown();
        # set the random color of the pen
        turtle.pencolor((randint(0, 255), randint(0,255), randint(0,255)));
        turtle.forward(15);
        
        turtle.penup();
        turtle.forward(15);

    # exit when click the screen
    screen.exitonclick();

if __name__ == "__main__":
    main();
            

