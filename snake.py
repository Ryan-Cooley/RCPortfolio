# Snake Game
# This code is for educational/demo purposes and is a simple implementation of the classic Snake game.

from turtle import Screen
from snake_game_classes import *
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoring = Scoring()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
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
        snake.head.xcor() > 285
        or snake.head.xcor() < -285
        or snake.head.ycor() > 285
        or snake.head.ycor() < -285
    ):
        game = False
        break

    # Tail Collision
    for seg in snake.segs[1:]:
        if snake.head.distance(seg) < 10:
            game = False
            break

scoring.game_over()
scoring.score = 0
scoring.update_writing()
screen.exitonclick()

