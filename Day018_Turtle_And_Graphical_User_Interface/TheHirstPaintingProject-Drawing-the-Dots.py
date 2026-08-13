import turtle as turtle_module
import random

turtle_module.colormode(255)
tom = turtle_module.Turtle()
tom.speed(speed = "fastest")
tom.penup()
tom.hideturtle()
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
tom.setheading(225)
tom.forward(300)
tom.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)
    if dot_count % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()

"""
import turtle as t
import random

tom = t.Turtle()

t.colormode(255)
# t.speed(speed = "fast")
color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
spot_dist = 50
tom.teleport(x = -250, y = -200)

for row in range(1, 11):
    print(tom.position())
    for col in range(1, 11):
        tom.dot(20, random.choice(color_list))
        tom.penup()
        if col == 10:
            tom.teleport(x = -250, y= -200 + (spot_dist * row))
        elif col != 10:
            tom.forward(spot_dist)
            tom.pendown()


screen = t.Screen()
screen.exitonclick()
"""