from turtle import Turtle

MOVE_DIST = 50

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def left_side(self):
        self.backward(MOVE_DIST)

    def right_side(self):
        self.forward(MOVE_DIST)