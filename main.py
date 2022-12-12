from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import Block
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=700, height=600)
screen.bgcolor("black")
screen.title("BREAKOUT GAME")
screen.tracer(0)

paddle = Paddle((0, -275))
ball = Ball()
blocks = Block()
score = Scoreboard(3)

screen.listen()
screen.onkey(paddle.left_side, "Left")
screen.onkey(paddle.right_side, "Right")
screen.onkey(paddle.left_side, "w")
screen.onkey(paddle.right_side, "s")


def check_collision_with_blocks():
    for block in blocks.blocks:
        if ball.distance(block) < 30:
            block.quantity -= 1
            if block.quantity == 0:
                block.clear()
                block.goto(3000, 3000)
                blocks.blocks.remove(block)
                score.point()

            # detect collision from left
            if ball.xcor() < block.left_wall:
                ball.bounce_x()

            # detect collision from right
            elif ball.xcor() > block.right_wall:
                ball.bounce_x()

            # detect collision from bottom
            elif ball.ycor() < block.bottom_wall:
                ball.bounce_y()

            # detect collision from top
            elif ball.ycor() > block.upper_wall:
                ball.bounce_y()

on_game = True


while on_game:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # DETECTION WITH THE TOP WALL
    if ball.ycor() > 270:
        # needs to bounce
        ball.bounce_y()

    # DETECTION WITH THE BOTTOM WALL
    if ball.ycor() < -270:
        ball.reset_position()
        score.decrease_lives()
        if score.lives < 1:
            score.game_over()
            on_game = False
        ball.bounce_y()

    # DETECTION WITH PADDLES
    if ball.distance(paddle) < 30 and ball.ycor() < -250:
        ball.bounce_y()

    # DETECTION WITH RIGHT WALL
    if ball.xcor() > 340:
        ball.bounce_x()

    # DETECTION WITH LEFT WALL
    if ball.xcor() < -340:
        ball.bounce_x()

    check_collision_with_blocks()


screen.exitonclick()
