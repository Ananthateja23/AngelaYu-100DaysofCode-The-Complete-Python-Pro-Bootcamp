# method02: Tutorial approach
# Import turtle and random modules
import turtle as t
import random

# Create a Turtle object
tim = t.Turtle()

# set the color mode
t.colormode(cmode = 255)

# A function definition to generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# directions holds east(0) north(90) west(180) south(270)
directions = [0, 90, 180, 270]

# sets pensize of turtle
tim.pensize(width = 15)
# sets the speed of turtle
tim.speed("fastest")

# logic to draw a random walk
for _ in range(200):
    # tim.color(random.choice(colors))
    tim.color(random_color())
    tim.forward(30) 
    tim.setheading(random.choice(directions))

# Holds the canvas screen
screen = t.Screen()
screen.exitonclick()
"""
method01: self explored approach

import turtle as t
import random

genie = t.Turtle()
screen = t.Screen()

genie.speed(speed = 10)
genie.pensize(width = 10)

directions = [0, 90, 180, 270]
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for _ in range(20):
    genie.color(random.choice(colors))
    genie.forward(25)
    genie.setheading(random.choice(directions))

screen.exitonclick()
"""