from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
Scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    # Detect collison with food
    if snake.head.distance(food) < 15:
        snake.extend_snake()
        Scoreboard.increase_score()
        food.refresh()

    # Detect collison with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        Scoreboard.game_over()
        is_game_on = False

    # Detect collison with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            Scoreboard.game_over()

screen.exitonclick()