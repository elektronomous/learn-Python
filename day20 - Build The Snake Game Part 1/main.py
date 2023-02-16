from turtle import Screen, Turtle
from random import choice
import time

# create a screen
screen = Screen();
# set the height and width.
screen.setup(width=800, height=800);
# set the screen background
screen.bgcolor("black");
# set the title of the window screen
screen.title("Snake Game");
# colors
# colors = ["red", "white", "blue", "green", "yellow"];
# there's delay animation when you move the object, it make the object
# lag when moving. turn off the animation
screen.tracer(0);

"""


                |
                |
                |
                |  This our turtle (by default has width=40 & height=40)
                |  /
                | /
_______________|||____________________
               |||
                |
                |
                |
                |
                |
                |

= To make the snake, you need to create three object in order
    
"""
# create three turtles that has square shape
def create_body_snake():
    # create snakes body
    snakes = [];
    # by default the square object has 40x40 pixel element.
    # to create the tails, you need to places the other object before the 20 pixel of the first head
    pos_before_head = -20;
    
    for _ in range(3):
        # create one head, with two tails
        snake = Turtle("square");
        snake.color("white");
        snake.penup();
        snake.setposition(x=pos_before_head * _, y=0);
        
        snakes.append(snake);
    
    # manually
    return snakes;


def main():
    snakes = create_body_snake();
    
    playing = True;
    
    while playing:
        # when you turn off the screen animation, you must update the screen animation
        screen.update();
        time.sleep(1);
        # make the snake move
        # move from the back - front
        for n in range(len(snakes)-1, 0, -1):
            xcord_front_tail = snakes[n - 1].xcor();
            ycord_front_tail = snakes[n - 1].ycor();
            # then set the tail
            snakes[n].goto(xcord_front_tail, ycord_front_tail);    
        snakes[0].forward(20);
        snakes[0].left(45);

if __name__ == "__main__":
    main();

# exit the screen when you click on it.
screen.exitonclick();