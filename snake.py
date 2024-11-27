# Snake Game

from turtle import Screen
from snake_game_classes import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

box = Turtle()
box.color("white")
box.penup()
box.hideturtle()
box.goto(-305, -300)
box.pendown()
box.pensize(30)  # Set the pen size for better visibility
box.fillcolor("black")  # Set the fill color to black

box.begin_fill()
box.left(90)
box.forward(605)
box.right(90)
box.forward(600)
box.end_fill()

snake = Snake()
food = Food()
scoring = Scoring()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game= True
while game:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Food Collisions
    if snake.head.distance(food) < 15:
        food.new_place()
        snake.longer()
        scoring.add_to_score()

    # Wall Collision
    if (
        snake.head.xcor() > 280 #CORRECT
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280 #CORRECT
    ):
        game = False
        break

    # Tail Collision
    for seg in snake.segs[1:]:
        if snake.head.distance(seg) < 10:
            game = False
            break

scoring.game_over()
screen.exitonclick()

