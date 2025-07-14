# Snake Game Classes
# This code is for educational/demo purposes and is a simple implementation of the classic Snake game.

from turtle import Turtle
import random

start = [(0, 0), (-20, 0), (-40, 0)]
MOVING = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
FOOD_MARGIN = 25  # Margin to keep food away from the wall

class Snake:
    def __init__(self):
        self.segs = []
        self.make_snake()
        self.head = self.segs[0]

    def make_snake(self):
        for pos in start:
            self.add_seg(pos)

    def add_seg(self, pos):
        seg = Turtle("square")
        seg.color("light blue")
        seg.penup()
        seg.goto(pos)
        self.segs.append(seg)

    def longer(self):
        """Make the snake one segment longer"""
        self.add_seg(self.segs[-1].pos())

    def move(self):
        for i in range(len(self.segs) - 1, 0, -1):
            x, y = self.segs[i - 1].position()
            self.segs[i].goto(x, y)
        self.head.forward(MOVING)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.new_place()

    def new_place(self):
        rx = random.randint(-285 + FOOD_MARGIN, 285 - FOOD_MARGIN)
        ry = random.randint(-285 + FOOD_MARGIN, 285 - FOOD_MARGIN)
        self.goto(rx, ry)

class Scoring(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_writing()

    def update_writing(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", 
        font=("Courier", 20, "normal"))

    def add_to_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_writing()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER :(", align="center", 
        font=("Courier", 30, "normal"))
        
