from turtle import Turtle

START_POSITION = (-250, 270);
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__();
        self.penup();
        self.level = 1;
        self.hideturtle();
        self.goto(START_POSITION);
        self.write(f"level {self.level}", False, "Center", ("Gintronic", 10, "normal"));
    
    def increase_level(self):
        self.level += 1;
        self.clear();
        self.goto(START_POSITION);
        self.write(f"level {self.level}", False, "Center", ("Gintronic", 10, "normal"));
    
    def game_over(self):
        self.clear();
        self.goto(START_POSITION);
        self.write(f"level {self.level}", False, "Center", ("Gintronic", 10, "normal"));
        self.goto((0,0));
        self.write(f"Game Over", False, "Center", ("Gintronic", 10, "normal"));
    
    def get_level(self):
        return self.level;