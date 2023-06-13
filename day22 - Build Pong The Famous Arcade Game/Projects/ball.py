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
        # we start from speed = 15
        self.directions = [choice([-INITIAL_SPEED+1,INITIAL_SPEED-1]), choice([-INITIAL_SPEED,INITIAL_SPEED])];
        self.x, self.y = [0,0];
    
    def move(self):
           # check if the ball hit the CEILING
           if self.y >= CEILING or self.y <= FLOOR:
               self.change_directions('y');
           # debug only
           # if self.x >= X_DEFAULT_POSITION or self.x <= X_LEFT_DEF_POSITION:
           #    self.change_direction('x');
               
           # setposition of the ball
           self.setposition(self.x,self.y);
           # move the position again
           self.x += self.directions[0];
           self.y += self.directions[1];
           
               
    
    def change_directions(self, direction:str):
        if direction == 'x':
            self.directions[0] *= -1;
        else:
            self.directions[1] *= -1;
    
    def get_directions(self):
        if self.x < 0:
            return "left";
        else:
            return "right";
        