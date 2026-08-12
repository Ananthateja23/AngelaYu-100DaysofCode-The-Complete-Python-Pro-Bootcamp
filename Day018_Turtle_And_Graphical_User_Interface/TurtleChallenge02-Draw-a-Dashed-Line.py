# from turtle import Turtle, Screen
import turtle as t

genie_turtle = t.Turtle()

# genie_turtle.hideturtle()
# for _ in range(15):
#     genie_turtle.forward(10)
#     genie_turtle.color("white")
#     genie_turtle.forward(10)
#     genie_turtle.color("black")

for _ in range(15):
    genie_turtle.forward(10)
    genie_turtle.penup()
    genie_turtle.forward(10)
    genie_turtle.pendown()


# screen = Screen()
# screen.exitonclick()