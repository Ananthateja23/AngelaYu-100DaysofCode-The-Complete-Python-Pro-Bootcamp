# Topic: Turtles racing game
"""
I'm going to presume that you've already had a play around with it 
and you know exactly how it works. 
Now, the other thing that we saw a lot of in this project is this concept of having
multiple objects created from the same class. 
So in this case, we're using the turtle class to construct a turtle object called Timmy,
but we've also got a separate object called Tommy. And Timmy and Tommy are both
Tuttle objects, but they're different instances. So they can act independently,
they can have different appearances, they can have different colors,
different attributes, and also a different speed of movement.
So we've seen in our turtle race that each of these instances can act of their
own accord and have different state.
And that's shown in the different speed of movement and this capability of
creating multiple objects which can act and behave independently
is really the secret to why Object Oriented Programming can be so
powerful.
We can create so many of these objects and get them to do our bidding in various
parts of our program
"""

# Import the necessary modules
from turtle import Turtle, Screen
import random

# Creating a screen object and set the screen properties

screen = Screen()
screen.setup(width = 500, height = 400)
is_race_on = True
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# logic to create multiple turtle objects
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape ="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x = -230, y = y_positions[turtle_index])
    all_turtles.append(new_turtle)

# check the users input
if user_bet:
    is_race_on = True

# logic for turtles racing game
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle_color = turtle.pencolor()
            if winning_turtle_color == user_bet:
                print(f"You've win! The {winning_turtle_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_turtle_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# holds the canvas screen
screen.exitonclick()
