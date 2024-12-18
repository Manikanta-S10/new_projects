from turtle import Turtle,Screen
from timmy import Timmy
from car_maneger import Car
from levels import Level
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.title('My Game')
screen.listen()

timmy = Timmy()
car = Car()
level = Level()
screen.onkey(timmy.move_up,'Up')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move_car()

    # Detect collision with car
    for i in car.all_cars:
        if timmy.distance(i) < 20:
            is_game_on = False 

    # If turtle reached another end
    if timmy.ycor() > 280:
        timmy.starting_point()
        level.next_level()
        car.level_up()





screen.exitonclick()
