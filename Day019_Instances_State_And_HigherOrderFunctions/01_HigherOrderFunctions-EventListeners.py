# Topic: Higher order functions and Event Listeners
# Higher order function?
# idea of HOF is  A function that can work with other functions
# Event listener?
# when the user taps a specific key on the keyboard
# and the code that allows us to do are called event listeners


# Import the necessary modules
from turtle import Turtle, Screen

# Create a Turtle and Screen Objects
tom = Turtle()
screen = Screen()

# function executes when users hits the particular key
def move_forward():
    tom.forward(10)

# Event listener
screen.listen()
# Binding function to the user keyboard strokes
screen.onkey(key = "space", fun = move_forward)
# hold the canvas screen
screen.exitonclick()
