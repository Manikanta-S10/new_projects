import colorgram
from turtle import *
import random

# Extarcting color values from the image (spot haist painting) using cologram lib
color_list = []
colors = colorgram.extract('haistpainting/spot haist painting.jpeg',30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_list.append((r,g,b))
print(color_list)    

# initalize the turtle 
tim = Turtle()
#To get rgb values set colormode to 255
colormode(255)
#To speed up the turtle
tim.speed('fastest')
# To hide the turtle
tim.hideturtle()
#To hide the pen so that pen lines will not visible to user
tim.penup()

tim.setheading(225.0)
tim.fd(300)
tim.left(135)
number_of_dots = 100

for dot_count in range(1,number_of_dots+1):
    tim.dot(10,random.choice(color_list))
    tim.fd(50)
    

    if dot_count % 10 == 0:
        tim.left(90)
        tim.fd(40)
        tim.left(90)
        tim.fd(500)
        tim.right(180)
    
    



screen = Screen()
screen.exitonclick()

