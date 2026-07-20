from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []

starting_pos = [(0, 0), (-20, 0), (-40, 0)]

for _ in range(3):
    snake = Snake(starting_pos[_])
    segments.append(snake)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    segments[0].move(segments)

screen.exitonclick()
