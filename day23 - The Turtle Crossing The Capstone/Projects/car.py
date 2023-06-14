from turtle import Turtle, Screen
from random import choice

START_POSITION_y = -250;
START_POSITION_x = -310;
DISSAPEAR_POSITION_x = -320;
DEF_PIXEL = 15;
N_CARS = 34;
CAR_COLOUR = ["brown", "cyan", "orange", "gold", "maroon", "red", "yellow", "blue", "purple"];

class Car:
    def __init__(self):
        self.cars = [];
        self.generate_cars();
    
    def generate_cars(self):
        # we create N_CARS cars        
        for y in range(N_CARS):
            car = Turtle("square");
            # turn off the draw mode
            car.penup();
            # turn into circle
            car.shape("square");
            # get the black color
            car.color("black");
            # get the start position
            car.goto(START_POSITION_x, START_POSITION_y + (y * DEF_PIXEL));
            # stretch it a little bit
            car.shapesize(stretch_len=2);
            # choose the color
            car.color(choice(CAR_COLOUR));
            # change the animation
            car.speed("fastest");
            # append it to the cars
            self.cars.append(car);
    
    def random_move(self):
        the_car = choice(self.cars);
        the_car.goto(the_car.xcor() - DEF_PIXEL, the_car.ycor());
        if the_car.xcor() < DISSAPEAR_POSITION_x:
            self.reset_position(the_car);
    
    def reset_position(self, the_car):
        # reset from left again
        the_car.goto(abs(START_POSITION_x), the_car.ycor());
        # then pick another colors
        the_car.color(choice(CAR_COLOUR));
    
    def get_cars(self):
        return self.cars;