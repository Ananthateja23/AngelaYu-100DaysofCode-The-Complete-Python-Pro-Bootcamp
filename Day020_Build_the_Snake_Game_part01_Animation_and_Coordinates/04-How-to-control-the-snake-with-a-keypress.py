# step01: Create a snake body
# step02: move the snake
# step03: Control the snake

# Import necessary modules
from turtle import Screen
from snake import Snake
import time

# create screen instance and set screen properties
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# It is very important to disable the animation effect
screen.tracer(0) # disable the animation

# create a snake instance
# It creates three segment snake
snake = Snake()

# Event listeners
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# logic to move the snake
# Note: if any doubt in logic, just rewatch video
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# holds the popped up window
screen.exitonclick()