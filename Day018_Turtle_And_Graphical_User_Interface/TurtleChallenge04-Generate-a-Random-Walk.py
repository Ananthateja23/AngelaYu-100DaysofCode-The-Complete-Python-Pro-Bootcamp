# method02: Tutorial approach
import turtle as t
import random

tim = t.Turtle()
t.colormode(cmode = 255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]

tim.pensize(width = 15)
tim.speed("fastest")

for _ in range(200):
    # tim.color(random.choice(colors))
    tim.color(random_color())
    tim.forward(30) 
    tim.setheading(random.choice(directions))

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