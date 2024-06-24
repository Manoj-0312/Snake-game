from turtle import Screen
import time
from snake_class import Snake
from food_class import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game ")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
food.random_food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    score.score_keeper()
    if snake.head.distance(food)<20:
        score.clear()
        snake.new_tur()
        food.random_food()
        score.score +=1
        score.score_keeper()
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        score.game_over()
        game_on = False
    for i in snake.turtles[1:]:
        if snake.head.distance(i)<15:
            score.game_over()
            game_on =False
screen.exitonclick()
