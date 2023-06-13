from turtle import Turtle
from square import *

class ScoreBoard(Turtle):
    def __init__(self):
        self.score_left = 0;
        self.score_right = 0;
        # create scoreboard
        super().__init__();
        # hide the turtle and make the center dashed-line
        self.hideturtle();
        # we're going to make the dashed-line drawn from above to bottom
        self.setheading(BOTTOM);
        # from top to bottom of the screen
        self.penup();
        # set the color of the scoreboard
        self.color("white");
        # set the animation, we dont need to blink
        self.speed("fastest");
        
        self.refresh();
    
    def refresh(self):
        self.clear();
        self.pensize(5);
        
        # for the dashed line
        self.setposition(X_DASHED_LINE, Y_DASHED_LINE);
                
        for n in range(round(screen_height / square_height)):
            if not (n%2):
                self.pendown();
            else:
                self.penup();
            self.forward(square_height);
        self.penup();
            
        # for the left score's number
        self.setposition(-X_SCORE_DEFAULT_POSITION, Y_SCORE_DEFAULT_POSITION);
        self.write(f"{self.score_left}", False, "center", font=("Gintronic", 30, "bold"));
        # for the right score's number
        self.setposition(X_SCORE_DEFAULT_POSITION, Y_SCORE_DEFAULT_POSITION);
        self.write(f"{self.score_right}", False, "center", font=("Gintronic", 30, "bold"));
    
    def increase_score(self, position):
        if position == "left":
            self.score_left += 1;
        else:
            self.score_right += 1;
        self.refresh();
    
    def winner(self, position):
        self.setposition(0, 0);
        if position == "left":
            self.write("GAME OVER. Left paddle is winner!", False, "center", font=("arial", 20, 'bold'));
        else:
            self.write("GAME OVER. Right paddle is winner!", False, "center", font=("arial", 20, 'bold'));
