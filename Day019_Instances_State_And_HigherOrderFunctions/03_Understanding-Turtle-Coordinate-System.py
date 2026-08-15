# Topic: Object state and Instances, Understanding the Turtle Coordinate System

# Import the necessary modules
from turtle import Turtle, Screen

# Create the screen instance and set properties
screen = Screen()
screen.setup(width=500, height=400)
# user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
# There is no issue if you uncomment "user_bet". It doesn't change the control flow
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# logic to create multiple turtle instances
for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-230, y=y_positions[turtle_index])

# holds the canvas screen
screen.exitonclick()
