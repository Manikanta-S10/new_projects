import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='make your bet',prompt='which turtle you want win? enter the color: ')
colors = ['red','yellow','blue','green','pink','grey','purple']
y_coordinate = [-50,-100,-150,0,50,100,150]
all_turtles = []

for turtle_index in range(0,7):
    new_turtle = turtle.Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y_coordinate[turtle_index])
    all_turtles.append(new_turtle)
    print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for tur in all_turtles:
        if tur.xcor() > 220:
            is_race_on = False
            winning_color = tur.pencolor()
            if user_bet == turtle:
                print(f"You've won the bet {winning_color} turtle has won.")
            else:
                print(f"You've lost the bet {winning_color} turtle has won.")  
        rand_distance = random.randint(0,10)
        tur.forward(rand_distance)

screen.exitonclick()