FONT = ("Arial", 24, "normal")
INC_LEVEL = 1

from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.set_turtle()
        
    def set_turtle(self):
        self.goto(-350,260)
        self.write(f'Level:{self.level}',False,'left',FONT)    

    def next_level(self):
        self.level += INC_LEVEL
        self.clear()
        self.set_turtle()
            


