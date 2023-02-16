from turtle import Turtle
from food import SAFE_HEIGHT

ADJUST_WIDTH = -25;

class Scoreboard(Turtle):
    def __init__(self):
        # we start from 0
        self.score = 0;
        # create scoreboard
        super().__init__();
        # we need to put a sentence "score = n" in the center of the screen.
        # according to the food position we get the default POSITION
        # this sape for debugging only
        # self.shape("square");
        # we dont need the turtle
        self.hideturtle();
        
        # self.shapesize(0.2, 0.2);
        # we dont draw, so turn off the draw mode
        self.penup();
        # set the color of the score
        self.color("green");
        self.refresh();
            
    def refresh(self):
        self.clear();
        self.setposition(x=ADJUST_WIDTH, y=SAFE_HEIGHT);
        self.write(f"Score = {self.score}", False, "center", font=('arial', 11, 'bold'));
    
    def game_over(self):
        self.setposition(0, 0);
        self.write("GAME OVER", False, "center", font=("arial", 20, 'bold'));