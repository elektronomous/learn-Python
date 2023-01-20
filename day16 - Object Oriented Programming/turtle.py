from turtle import Turtle, Screen

# Create a turtle object
my_turtle = Turtle();
# Create another turtle
another_turtle = Turtle();
# change its shape to turtle
another_turtle.shape("turtle");

print(my_turtle);

# when we create the object, why we get arrow as the object not a turtle
# you can change the shape to a turtle
my_turtle.shape("turtle");

# default color of your turtle is black, you could change it
my_turtle.color("DarkOliveGreen");

# show the screen where our turtle will draw
canvas_turtle = Screen();
# forward for 100 paces
my_turtle.forward(100);

# default screen window's size where our turtle will brush
print(canvas_turtle.canvheight);
# you click the canvas to exit
canvas_turtle.exitonclick();
