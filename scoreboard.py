from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.clear()
        self.goto(0,270)

    def write_shit(self):
        self.write(f"score: {self.score}", False, "center", ["Courier", 15, "normal"])

    def write_gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, "center", ["Courier", 20, "normal"])



