from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.goto(x=0, y=260)
        self.write(f"Level:{self.score}", align="center", font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Level:{self.score}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.write(f"Game Over", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
