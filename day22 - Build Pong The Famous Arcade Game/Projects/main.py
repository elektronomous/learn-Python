from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
from time import sleep
from square import *

def check_hit(the_ball, the_wall):
    for each_square in the_wall:
        if the_ball.distance(each_square) < 18:
            the_ball.change_directions('x');
            return True;
    return False;
            

def main():
    # set the screen
    screen = Screen();
    # set the widht, height
    screen.setup(width=600, height=600);
    # set the title
    screen.title("Ping Pong");
    # set the background
    screen.bgcolor("black");
    # turn off the animation delay
    screen.tracer(0);
    # playing status
    playing = True;
    # listen to the keyboard
    screen.listen();
    
    # create the left paddle
    left_paddle = Paddle("left");
    # create the right paddle
    right_paddle = Paddle("right");
    # create the ball
    ball = Ball();
    # create the scoreboard
    scoreboard  = ScoreBoard();
    
    # we play two player at the same time
    # so we listen on 4 keyboard event
    # each of 2 buttons assign to player 1
    # and the other to player 2
    
    # player 1 (left_paddle)
    # up
    screen.onkey(left_paddle.up,"w");
    # down
    screen.onkey(left_paddle.down,"s");
    
    # player 2 (right_paddle);
    # up
    screen.onkey(right_paddle.up, "Up");
    # down
    screen.onkey(right_paddle.down, "Down");
    
    while playing:
        screen.update();
        sleep(0.1);
        
        # ball move
        ball.move();
        
        # check if the ball hit the left paddle
        if check_hit(the_ball=ball, the_wall=left_paddle.get_paddle()):
            scoreboard.increase_score("left");
        # check if the ball hit the right paddle
        if check_hit(the_ball=ball, the_wall=right_paddle.get_paddle()):
            scoreboard.increase_score("right");
        
        
        # if the balls out, the game too
        if ball.xcor() > X_RIGHT_PADDLE_BUMP:
            scoreboard.winner('left');
            playing = False;
            
        if ball.xcor() < X_LEFT_PADDLE_BUMP:
            scoreboard.winner('right');
            playing = False;
    
    screen.exitonclick();

if __name__ == "__main__":
    main();