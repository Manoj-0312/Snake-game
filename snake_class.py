from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP =90
DOWN =270
RIGHT =0
LEFT =180


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def move(self):
        for index in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[index - 1].xcor()
            new_y = self.turtles[index - 1].ycor()
            self.turtles[index].goto(new_x, new_y)
        self.turtles[0].fd(MOVE_DISTANCE)

    def new_tur(self):
        xcor = self.turtles[len(self.turtles)-1].xcor()
        ycor = self.turtles[len(self.turtles) - 1].ycor()
        tur1= Turtle("circle")
        tur1.penup()
        tur1.goto(xcor,ycor)
        tur1.color("white")
        self.turtles.append(tur1)


    def create_snake(self):
        for i in STARTING_POSITION:
            tur = Turtle("circle")
            tur.penup()
            tur.color("white")
            self.turtles.append(tur)
            tur.goto(i)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

