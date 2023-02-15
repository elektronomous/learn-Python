from turtle import Turtle, Screen

# create a screen where turtle draw its pen
screen = Screen();
# create a turtle inside it
turtle = Turtle();
# change its shape
turtle.shape("turtle");

def clockwise():
    turtle.right(10);
def counter_clockwise():
    turtle.left(10);

def move_forward():
    turtle.forward(10);

def move_backward():
    turtle.backward(10);

def clear_screen():
    turtle.reset();

def main():
    # listen to the key event
    screen.listen();

    # triggered when 'w' is pressed
    screen.onkey(move_forward, "w");
    # triggered when 's' is pressed
    screen.onkey(move_backward, "s");
    # triggered when 'd' is pressed
    screen.onkey(clockwise, "d");
    # triggered when 'a' is pressed
    screen.onkey(counter_clockwise, "a"); 
    # triggered when 'c' is pressed
    screen.onkey(clear_screen, "c");

    # exit when click the screen
    screen.exitonclick();



if __name__ == "__main__":
    main();