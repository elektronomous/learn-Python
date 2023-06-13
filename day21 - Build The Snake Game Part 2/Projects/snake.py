from turtle import Turtle


# by default, the Turtle object that created on the middle Screen object has 20x20 pixel element
# so we can create the other object before the first created object on 20pixel x coordinate
TAIL_DEFAULT_POSITION = -20;
N_MOVEMENT = 20;

HEAD = 0;
TAIL = -1;

RIGHT = 0;
UP = 90;
LEFT = 180;
DOWN = 270;

class Snake:
    def __init__(self):
        self.snakes = [];
        """
        DIRECTION
                           90 up
                            |
                            |
                            |
        180 left ___________|____________ 0 right
                            |
                            |
                            |
                        270 down
        """
        self.direction = 0; # by default, right
        self.create_snake();
        self.head = self.snakes[HEAD];
        self.tail = self.snakes[TAIL];
    
    def create_snake(self):
        # we start by building a snake with 2 tails, with 1 head
        for n in range(3):
            snake_part = Turtle("square");
            # set the color of the snake
            snake_part.color("white");
            # turn off the draw mode
            snake_part.penup();
            # set the position of the first head to the 2 tails
            snake_part.setposition(x=TAIL_DEFAULT_POSITION * n, y=0);
            self.snakes.append(snake_part);
    
    def add_tail(self):
        # get the tails position
        tail_position = self.tail.position();
        
        snake_part = Turtle("square");
        # set the color of the snake
        snake_part.color("white");
        # turn off the draw mode
        snake_part.penup();
        # add tail to the current last tails position
        snake_part.setposition(tail_position);
        self.snakes.append(snake_part);

    def move(self):
        self.move_part();
        # move the head
        self.head.forward(N_MOVEMENT);
    
    def move_part(self):
        # we move the tail first, then the head.
        for n_part_of_the_snake in range(len(self.snakes)-1, 0, -1):
            # get the front part coordinate
            xcord_front_part = self.snakes[n_part_of_the_snake-1].xcor();
            ycord_front_part = self.snakes[n_part_of_the_snake-1].ycor();
            # move the backmost tails to the front tails
            self.snakes[n_part_of_the_snake].setposition(xcord_front_part, ycord_front_part);

    
    def change_direction(self, direction:int):
        self.move_part();
        self.head.setheading(direction);
        self.head.forward(N_MOVEMENT);
            
    
    # you can't move the right to left vice versa, also with up and down.
    def up(self):
        # if the snake heading position not crossed the UP position        
        if not self.head.heading() == DOWN:
            # set the snake heading
            self.change_direction(UP);
            

    def down(self):
        if not self.head.heading() == (UP):
            self.change_direction(DOWN);
    
    def left(self):
        if not self.head.heading() == (RIGHT):
            self.change_direction(LEFT);
    
    def right(self):
        if not self.head.heading() == (LEFT):
            self.change_direction(RIGHT);