from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = lives
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"score: {self.score} | lives: {self.lives}", align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.update_score()

    def decrease_lives(self):
        self.game_over()
        self.lives -= 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0, -50)
        self.write(f"GAME OVER. Your Score: {self.score}", align=ALIGNMENT, font=FONT)