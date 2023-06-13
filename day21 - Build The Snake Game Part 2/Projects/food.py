from turtle import Turtle
from random import randint
 
SAFE_HEIGHT = SAFE_WIDTH = 280;

# create the snake food
class Food(Turtle):
    def __init__(self):
        super().__init__();
        # after inheritate the Turtle class, you can use its method
        # self.shape("square");
        self.shape("circle");
        # we don't draw a line, so turn off the draw mode
        self.penup();
        # give the food size to 16pixel, by default it has 20pixel
        self.shapesize(stretch_len=0.8, stretch_wid=0.8);
        # give the food color
        self.color("yellow");
        # make the food animation faster, so we dont see the animation blink
        self.speed("fastest");
        """
        screen width = 600, height = 600
        
                                300
                +-------------------------------+
                |                               |
                |                               |
                |                               |
                |                               |
            300 |                               | 300
                |                               |
                |                               |
                |                               |
                |                               |
                |                               |
                +-------------------------------+
                                300
        = We dont create the food on the wall so, we substract the width and the height
        """ 
    
    def refresh(self):
        # create the food inside the screen in random way.
        self.setposition(x=randint(-SAFE_WIDTH, SAFE_WIDTH), y=randint(-SAFE_HEIGHT, SAFE_HEIGHT));