from turtle import Turtle, Screen
from random import randint

def main():
    # create a screen where our turtle will draw with its brush
    screen = Screen();
    # create a turtle object
    my_turtle = Turtle();
    # we set this so we can use from 0 - 255 to set the color of the pen
    screen.colormode(255);
    # change its shape to turtle
    my_turtle.shape("turtle");
    # change the thickness of the pen
    my_turtle.pensize(5);

    # draw a square
    for _ in range(4):    
        # change the color on its turn
        my_turtle.color((randint(0,255), randint(0,255), randint(0,255)));        
        my_turtle.right(90);
        my_turtle.forward(100);

    # click the screen to exit
    screen.exitonclick();

if __name__ == "__main__":
    main();