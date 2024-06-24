from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")

    def score_keeper(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(0,270)
        self.write(f"Score is {self.score}", align='center', font=('courier', 20, 'normal'))

    def game_over(self):
        self.color("white")
        self.hideturtle()
        self.goto(0,0)
        self.write("GAME OVER",align='center', font=('courier', 30, 'normal'))
