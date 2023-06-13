from turtle import Turtle
from square import square_height
from square import *

Y_DEFAULT_POSITION = [square_height,0,-square_height];

class Paddle:
    def __init__(self, INIT_POSITION="left"):
        self.paddle = [];
        self.init_position = INIT_POSITION; 
        self.create_paddle();
        self.head, self.tail = self.paddle[0], self.paddle[len(self.paddle)-1];
        self.set_initposition();

    def create_paddle(self):
        for _ in range(3):
            # create the three square 
            square = Turtle("square");
            # don't pen mode
            square.penup();
            # give each square a color
            square.color("white");
            # append so we formed paddle
            self.paddle.append(square);
    
    def set_initposition(self):
        for n in range(len(self.paddle)):
            self.paddle[n].setposition(X_LEFT_DEF_POSITION if \
                                       self.init_position == "left" \
                                       else X_DEFAULT_POSITION,
                                       Y_DEFAULT_POSITION[n]);
    
    def update_position(self, n_movement):
        for square in self.paddle:
            square.sety(square.ycor() + n_movement);
            
    def up(self):
        if self.head.ycor() < CEILING:
            self.update_position(square_height);
    
    def down(self):
        if self.tail.ycor() > FLOOR:
            self.update_position(-square_height);
            
