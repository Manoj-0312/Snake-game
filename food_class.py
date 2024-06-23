from turtle import Turtle
import random ad ra


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed(0)
        self.color("cyan")

    def random_food(self):
        x= ra.randint(-280,280)
        y = ra.randint(-280, 280)
        self.goto(x,y)


