# Step01: Create the screen
# Step02: Create and move a paddle
# Step03: Create another paddle
# Step04: Create the ball and make it move
# Step05: Detect collision with wall and bounce
# Step06: Detect collision with paddle
# Step07: Detect when paddle misses
# Step08: Keep score

# Import the necessary modules
from turtle import Screen

# create a screen instance and set its properties
screen = Screen()

# It sets the window screen size
screen.setup(width = 800, height = 600)

# It sets the window background color
screen.bgcolor("black")

# It sets window screen title
screen.title("My Pong Game")

# It holds the popped up window screen
screen.exitonclick()