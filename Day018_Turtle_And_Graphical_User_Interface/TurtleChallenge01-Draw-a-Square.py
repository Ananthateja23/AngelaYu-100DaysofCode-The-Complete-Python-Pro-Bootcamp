# Import turtle module
from turtle import Turtle, Screen

# Create a Turtle object
genie = Turtle()

# logic to draw square
for _ in range(4):
    genie.right(90)
    genie.forward(100)


# Holds the canvas screen
screen = Screen()
screen.exitonclick()
