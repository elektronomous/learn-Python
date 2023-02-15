import colorgram
from turtle import Turtle, Screen
from random import choice


def main():
    # create a screen where the turtle would draw its pen
    screen = Screen();
    # create a turtle inside the screen
    turtle = Turtle();
    # create its shape
    turtle.shape("turtle");
    # change the thicknkess of the pen
    turtle.pensize(10);
    # set color mode to rgb 0.. 255
    screen.colormode(255);

    # extract colors from the image``
    colors = colorgram.extract("../Hirst.jpg", 100);

    y_pos = 0;
    
    for _ in range(100):
        # move up and draw the dots
        if not _ % 10:
            turtle.penup();
            turtle.setpos(0, y_pos);
            y_pos += 30;
            turtle.pendown();
        # pick the random color from colorgram
        color = choice(colors);
        turtle.pencolor(color.rgb.r, color.rgb.g, color.rgb.b);
        # create the dots.
        turtle.forward(1);
        # create the space
        turtle.penup();
        turtle.forward(30);
        turtle.pendown();
        

    # exit when click on screen
    screen.exitonclick();

if __name__ == "__main__":
    main();