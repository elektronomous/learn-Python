from turtle import Turtle, Screen

# create a screen where turtle would be draw
screen = Screen();
# create the turtle object inside the screen
turtle = Turtle();

def move_forwards():
    turtle.forward(10);

turtle.circle()

# listen to the key that get pressed
screen.listen();
# triggered the key to the turtle object
screen.onkey(move_forwards, "space");

# exit the screen when you click on it
screen.exitonclick();