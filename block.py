from turtle import Turtle
import random

colors = ['royal blue', 'blue', 'light blue', 'red', 'black', 'purple', 'aquamarine',
          'light steel blue', 'coral', 'crimson', 'light cyan', 'light sky blue', 'violet', 'salmon',
          'tomato', 'sandy brown', 'purple', 'deep pink', 'medium sea green', 'khaki' ]

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3,
           1, 1, 1, 4, 1, 3, 2, 2, 1, 2,
           1, 2, 1, 2, 1]

class Blocks(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=1, stretch_len=3)
        self.color(random.choice(colors))
        self.goto(x=x_cor, y=y_cor)
        self.quantity = random.choice(weights)

        # Defining borders of the blocks
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 15
        self.bottom_wall = self.ycor() - 15


class Block:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.blocks = []
        self.create_all_lanes()

    def create_lane(self, y_cor):
        for i in range(-550, 550, 60):
            block = Blocks(i, y_cor)
            self.blocks.append(block)

    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)
