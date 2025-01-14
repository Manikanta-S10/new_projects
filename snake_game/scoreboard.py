from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color('white')
        self.update_score()
        
    def update_score(self):
        self.write(f" score: {self.score} ",False, align=ALIGNMENT,font=FONT)  
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over',False,align=ALIGNMENT, font=FONT)

        
        
