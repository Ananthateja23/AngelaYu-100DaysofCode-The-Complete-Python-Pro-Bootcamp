# method02: Tutorial explained approach
# Import turtle and random module
import turtle as t
import random

# Create a Turtle object
tim = t.Turtle()

# Sets turtle speed
tim.speed(speed = "fastest")
# set turtle modules color mode
t.colormode(255)

# generates random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# Draw a spirograph
def draw_spirograph(size_gap):
    rotations = int(360 / size_gap)
    for _ in range(rotations):
        tim.color(random_color())
        tim.circle(radius = 100)
        tim.setheading(tim.heading() + size_gap)

draw_spirograph(size_gap = 5)

# Hold the canvas screen
screen = t.Screen()
screen.exitonclick()

"""
# method01: self explored approach
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(speed = "fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

position = tim.heading()
while position <= 360:
    print(position)
    tim.color(random_color())
    tim.circle(radius = 100)
    position += 5
    tim.setheading(position)

t.Screen().exitonclick()

"""