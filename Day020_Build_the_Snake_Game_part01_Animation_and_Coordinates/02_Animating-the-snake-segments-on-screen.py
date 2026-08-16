# step01: Create a snake body
# step02: move the snake

# Import necessary modules
from turtle import Screen, Turtle
import time

# create screen instance and set screen properties
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# It is very important to disable the animation effect
screen.tracer(0) # disable the animation


# list down starting positions of each square box
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

# logic to represent each square in its positions
# and also each new segment into segments
for position in starting_positions:
    new_segment = Turtle(shape = "square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# logic to move the snake
# Note: if any doubt in logic, just rewatch video
is_game_on = True
while is_game_on:
    """
    (box3)(box2)(box1)
    (empty)(box3 over box2)(box1)
    (empty)(box3)(box2 over box1)
    (empty)(box3)(box2)(box1)
    screen.update()
    # it accumulates the small actions(operations) and shows it at a time(ex. Gif images)
    # without screen.update(), nothing will visible on the screen 
    # even though we have a (while loop, for loop) operations are happening
    """
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(x = new_x, y = new_y)
    segments[0].forward(20)
    # segments[0].left(90)

# holds the popped up window
screen.exitonclick()