from turtle import Turtle, Screen
from random import randint

def main():
    # create a screen where the turtle would draw
    screen = Screen();
    # we set up our screen so we can decide the width and height
    screen.setup(width=500, height=400);
    # get the user turtle bet
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ");
    # create a colors of the turtle we're going to instance
    colors = ["red", "orange", "yellow", "green", "blue", "purple"];
    # create an list where our turtle would be stored
    turtles = {};

    
    # starting lineup
    starting_pos_x = -230;
    starting_pos_y = -100;

    for turtle_color in colors:
        turtles[turtle_color] = Turtle("turtle");
        turtles[turtle_color].color(turtle_color);
        # set its starting lineup
        turtles[turtle_color].penup();
        turtles[turtle_color].goto(starting_pos_x, starting_pos_y);
        starting_pos_y += 50;

    if user_bet in colors:
        race = True;
    else:
        race = False;
    
    while race:
        for turtle in turtles.items():
            # move forward randomly from 0 - 10;
            turtle[1].forward(randint(0, 10));

            

    # exit screen when click on it
    screen.exitonclick();

if __name__ == "__main__":
    main();