from snake import Snake
from turtle import Screen
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
    
    
    snake = Snake();
    
    
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

if __name__ == "__main__":
    main();
    