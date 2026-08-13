# from turtle import Turtle, Screen
# Import turtle module
import turtle as t

# Create Turtle object
genie_turtle = t.Turtle()

# genie_turtle.hideturtle()
# for _ in range(15):
#     genie_turtle.forward(10)
#     genie_turtle.color("white")
#     genie_turtle.forward(10)
#     genie_turtle.color("black")

# logic to draw a dashed line
for _ in range(15):
    genie_turtle.forward(10)
    genie_turtle.penup()
    genie_turtle.forward(10)
    genie_turtle.pendown()


# screen = Screen()
# screen.exitonclick()
# Holds the canvas screen
screen = t.Screen()
screen.exitonclick()