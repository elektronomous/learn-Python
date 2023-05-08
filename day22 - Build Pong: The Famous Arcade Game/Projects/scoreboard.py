from turtle import Turtle
from square import square_height, screen_height

X_SCORE_DEFAULT_POSITION = 120;
Y_SCORE_DEFAULT_POSITION = 255;
X_DASHED_LINE = 0;
Y_DASHED_LINE = 310;
BOTTOM = 270;

class Scoreboard(Turtle):
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