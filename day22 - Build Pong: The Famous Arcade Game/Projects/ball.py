from turtle import Turtle
from random import choice

from square import *

# create the ball
class Ball(Turtle):
    def __init__(self):
        # create the turtle
        super().__init__();
        # after inheritance the Turtle class, you can use its methods
        # change the shape into ball(circle)
        self.shape("circle");
        # dont drawing
        self.penup(); 
        # give it size
        self.shapesize(stretch_len=0.9, stretch_wid=0.8);
        # give the ball color
        self.color("red");
        # give the ball animation faster, so we don't see the ball blink
        self.speed("fastest");
        
        # get the direction randomly
        self.direction = [choice([-1,1]), choice([-1,1])];
        # then move
        self.move();
    
    def move(self):
           x, y = self.direction;
           # setposition of the ball
           self.setposition(x,y);
           # move the position again
           x += x;
           y += y;
               
    
    def change_direction(self):
        # hit the CEILING
        if self.ycor() >= CEILING:
            self.direction = self.directions[self.direction];
             