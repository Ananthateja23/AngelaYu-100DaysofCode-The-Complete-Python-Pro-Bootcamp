# Topic:  Make an Etch-A-sketch App
# Requirements
# W = Forwards, S = Backwards, A = Counterclockwise or leftwards, D = right or clockwise
# C = Clear drawing

"""
if you didn't manage to find some of the methods like home or clear.
It's a matter of getting practice with reading the documentation 
and having the patience to go through it and look for the relevant methods.
And on top of that, it's just a matter of messing around with the code.
Try things out, see what happens. And each time you add something, run the code,
see if it does what you want it to do. And if not, fix it.
And that is the endless cycle of software development.
So don't get frustrated if you got stuck.
As long as you managed to make it work in the end
and you've learned some lessons from this process,
then you can congratulate yourself on completing the job.
And I find that I always learn more when I make more mistakes
and when I struggle more. 
"""

# Import the necessary modules
from turtle import Turtle, Screen

# Create a Turtle instance and screen instance
tom = Turtle()
screen = Screen()

# functions to Etch-A-sketch
def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def clear_screen():
    # screen.reset()
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

def turn_right():
    #tom.right(10)
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)

def turn_left():
    # tom.left(10)
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)

# Event listener and corresponding function bindings
screen.listen()
screen.onkey(fun = move_forward, key = "w")
screen.onkey(fun = move_backward, key = "s")
screen.onkey(fun = turn_right, key = "d")
screen.onkey(fun = turn_left, key = "a")
screen.onkey(fun = clear_screen, key = "c")
# holds the canvas screen
screen.exitonclick()
