from turtle import Turtle
import random
COLORS = ['red','blue','pink','blue','green','purple','black','brown','grey']
CAR_MOVE_DISTANCE = 5
CAR_INCREMENT = 10

class Car():
    def __init__(self):
        self.all_cars = [] 
        self.car_speed = CAR_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240,250)
            new_car.goto(320,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += CAR_MOVE_DISTANCE


        

 

        




                



        
