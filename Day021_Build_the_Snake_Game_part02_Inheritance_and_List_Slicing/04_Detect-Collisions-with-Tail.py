# step01: Create a snake body
# step02: move the snake
# step03: Control the snake
# step04: detect collision with food
# step05: create a scoreboard
# step06: detect collision with wall
# step07: detect collision with tail

# Import necessary modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
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

# create a food instance
food = Food()

# create a scoreboard instance
scoreboard = ScoreBoard()

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

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # detect collision with tail
    # if head collides with any segment in the tail
    # trigger game over
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         is_game_on = False
    #         scoreboard.game_over()
    for segment in snake.segments[1:]:
       if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

# holds the popped up window
screen.exitonclick()