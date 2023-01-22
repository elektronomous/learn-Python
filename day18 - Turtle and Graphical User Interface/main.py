import colorgram
from turtle import Turtle, Screen


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
colors = colorgram.extract("Hirst.jpg", 100);

for color in colors:
    turtle.pencolor("")
# exit when click on screen
screen.exitonclick();