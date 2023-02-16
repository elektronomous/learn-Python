from snake import Snake
from turtle import Screen
from food import Food, SAFE_HEIGHT, SAFE_WIDTH
from scoreboard import Scoreboard
from time import sleep


def main():
    # set the screen
    screen = Screen();
    # set the width, height
    screen.setup(width=600, height=600);
    # set the title
    screen.title("Snake Game");
    # set the background to black
    screen.bgcolor("black");
    # turn off the animation delay
    screen.tracer(0);
    # playing status default to True
    playing = True;
    # listen on the key event
    screen.listen();
    
    # create the snake
    snake = Snake();
    # create its food
    food = Food();
    # create the scoreboard
    scoreboard = Scoreboard();
    
    # up
    screen.onkey(snake.up, "Up");
    # down
    screen.onkey(snake.down, "Down");
    # right
    screen.onkey(snake.right, "Right");
    # left
    screen.onkey(snake.left, "Left");
    
    while playing:
        screen.update();
        sleep(0.1);
        
        snake.move();
        
        # when the snakes get the food
        if snake.head.distance(food) < 18:
            food.refresh();
            scoreboard.score += 1;
            scoreboard.refresh();
            # grow the tails of the snake
            snake.add_tail();
            
        # when the snakes hit the wall
        if snake.head.xcor() > SAFE_WIDTH or snake.head.xcor() < -300 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
           # turn off the game
           playing = False; 
           scoreboard.game_over();
        
        # detect colission with the tails
        for tail in snake.snakes[:1]:
            # because the first iterator will be the head
            # if tail == snake.head:
            #     # we pass
            #     pass;
            if snake.head.distance(tail) < 10:
                playing = False;
                scoreboard.game_over();
    
    screen.exitonclick();

if __name__ == "__main__":
    main();
    