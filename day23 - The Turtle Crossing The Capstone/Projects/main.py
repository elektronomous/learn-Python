from turtle import Screen, Turtle
from player import Player
from car import Car
from scoreboard import Scoreboard
from time import sleep

START_TIME = 1;

def check_hit(player, the_cars):
    for each_car in the_cars:
        if player.distance(each_car) < 20:
            return True;
    return False;

def main():
    # we first created the screen
    screen = Screen();
    # set the width and the height
    screen.setup(width=600, height=600);
    # set the delay animation, so we can create the game
    screen.tracer(0);
    
    # then we create the player
    player_1 = Player();
    cars = Car();
    scoreboard = Scoreboard();
    playing = True;
    
    screen.listen();
    
    screen.onkey(player_1.up, "Up");
    screen.onkey(player_1.down, "Down");
    
    increase_time = START_TIME;
    
    while playing:
        sleep(increase_time);
        screen.update();
        cars.random_move();
        
        # check if the turtle get hit by the car
        if check_hit(player_1, cars.get_cars()):
            scoreboard.game_over();
            playing = False;
        
        if player_1.ycor() > 250:
            scoreboard.increase_level();
            player_1.reset_position();
            increase_time /= scoreboard.get_level();
    screen.exitonclick();


if __name__ == "__main__":
    main();