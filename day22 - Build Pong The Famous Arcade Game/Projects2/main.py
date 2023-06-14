from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep


screen = Screen();
screen.bgcolor("black");
screen.setup(width=800, height=600);
screen.title("Pong");
screen.tracer(0);
screen.listen();

r_paddle = Paddle((350, 0));
l_paddle = Paddle((-350, 0));
ball = Ball();


screen.onkey(r_paddle.go_down, "Down");
screen.onkey(r_paddle.go_up, "Up");
screen.onkey(l_paddle.go_down, "s");
screen.onkey(l_paddle.go_up, "w");

while True:
    screen.update();
    sleep(0.1);
    ball.move();


screen.exitonclick();