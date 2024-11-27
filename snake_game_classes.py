#Snake Game Classes

from turtle import Turtle
import random

start = [(0, 0), (-20, 0), (-40, 0)]
MOVING = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        rx = random.randint(-280, 280)
        ry = random.randint(-280, 280)
        self.goto(rx, ry)


class Scoring(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, -285)
        self.update_writing()
        self.hideturtle()

    def update_writing(self):
        self.write(f"Score: {self.score}", align="center", 
        font=("Courier", 20, "normal"))

    def add_to_score(self):
        self.clear()
        self.score += 1
        self.update_writing()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER :(", align="center", 
        font=("Courier", 30, "normal"))
        
