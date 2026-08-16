# Import necessary modules
from turtle import Screen, Turtle

# create screen instance and set screen properties
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# all_turtles = []
# x_coordinates = [0, -20, -40]
# for turtle_index in range(3):
#     new_turtle = Turtle(shape = "square")
#     new_turtle.color("white")
#     new_turtle.goto(x = 0 + x_coordinates[turtle_index], y = 0)
#     all_turtles.append(new_turtle)
#
# print(all_turtles)

# step01: Create a snake body

# list down starting positions of each square box
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# logic to represent each square in its positions
for position in starting_positions:
    new_segment = Turtle(shape = "square")
    new_segment.color("white")
    new_segment.goto(position)

# holds popped up window screen
screen.exitonclick()