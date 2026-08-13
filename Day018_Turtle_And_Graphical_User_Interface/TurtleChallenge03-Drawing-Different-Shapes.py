# Import turtle and random module
import turtle as t
import random

# Create a Turtle Object
genie = t.Turtle()

# search "turtle colors python"
# go to(click on) "colors Trinket"
# select the colors

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# function definition to draw different shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for side in range(num_sides):
        genie.forward(100)
        genie.right(angle)

# loop generates nums 3 to 11 for each polygon
for shape_side_n in range(3, 11):
    genie.color(random.choice(colors))
    draw_shape(shape_side_n)

"""
from turtle import Turtle, Screen, colormode
import random
ANGLE = 360

genie = Turtle()
colormode(255)

for side in range(3, 11):
    start_draw = side
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    genie.pencolor(r, g, b)
    while start_draw > 0:
        genie.right(ANGLE / side) # use only "/" not "//"
        genie.forward(100)
        start_draw -= 1
  
screen = Screen()
screen.exitonclick()
"""