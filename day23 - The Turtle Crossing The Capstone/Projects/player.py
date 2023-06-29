from turtle import Turtle

PLAYER_STEP = 10;
START_POSITION = (0, -280);

class Player(Turtle):
    def __init__(self):
        # we invoke the superclass so we can use its properties
        super().__init__();
        # turn it into turtle
        self.shape("turtle");
        # turn off the draw mode
        self.penup();
        # change directions to 90 degree
        self.setheading(90);
        self.goto(START_POSITION);
        
        
    def reset_position(self):
        self.goto(START_POSITION);
        self.setheading(90);
    
    def up(self):
        self.setposition(self.xcor(), self.ycor() + PLAYER_STEP);
    
    def down(self):
        self.setposition(self.xcor(), self.ycor() - PLAYER_STEP);