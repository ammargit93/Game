from turtle import Screen
from Snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scrbrd = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scrbrd.write_shit()

    if snake.segment[0].distance(food) < 15:
        food.refresh()
        scrbrd.score += 5
        snake.extend()
        scrbrd.clear()

    if snake.segment[0].xcor() > 280 or snake.segment[0].xcor() < -300 or snake.segment[0].ycor() < -280 or snake.segment[0].ycor() > 280:
        game_is_on = False
        scrbrd.write_gameover()

    for segment in snake.segment[1:]:
        if snake.segment[0].distance(segment) < 5:
            game_is_on = False
            scrbrd.write_gameover()


screen.exitonclick()
