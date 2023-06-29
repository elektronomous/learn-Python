from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen();
screen.bgcolor("black");
screen.setup(width=800, height=600);
screen.title("Pong");
screen.tracer(0);
screen.listen();

r_paddle = Paddle((350, 0));
l_paddle = Paddle((-350, 0));
ball = Ball();
scoreboard = Scoreboard();

screen.onkey(r_paddle.go_down, "Down");
screen.onkey(r_paddle.go_up, "Up");
screen.onkey(l_paddle.go_down, "s");
screen.onkey(l_paddle.go_up, "w");

screen.exitonclick();

while True:
    screen.update();
    # to make it speed, change 0.1 to 0.01 even faster to 0.0000.. 1
    sleep(0.1);
    ball.move();
    
    # when the ball hit the ceiling or floor
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y();

    # if the ball hit the paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x(); 
    
    # if the ball go through the wall and the paddle
    if ball.xcor() > 380:
        ball.reset_position();
        scoreboard.l_point();
        
    if ball.xcor() < -380:
        ball.reset_position();
        scoreboard.r_point();
