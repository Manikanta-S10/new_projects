from turtle import Turtle
TURTLE_HEADING = 90
TURTLE_MOVE_DISTANCE = 20
STARTING_POINT = (0,-280)

class Timmy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.starting_point()
        self.setheading(TURTLE_HEADING)

    def move_up(self):
        self.forward(TURTLE_MOVE_DISTANCE)

    def starting_point(self):
        self.goto(STARTING_POINT)    



