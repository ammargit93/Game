from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        xfood = random.randint(-280, 280)
        yfood = random.randint(-280, 280)
        self.goto(xfood, yfood)


