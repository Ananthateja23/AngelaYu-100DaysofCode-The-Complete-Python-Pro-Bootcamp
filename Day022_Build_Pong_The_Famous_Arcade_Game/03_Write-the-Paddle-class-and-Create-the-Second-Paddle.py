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
from paddle import Paddle

# create a screen instance and set its properties
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0) # disable the animation
# Remember that when you turn off the animation,
# you have to manually update the screen and refresh it every single time. 

# create the paddle instances
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


# logic to move the paddles up and down
screen.listen()
screen.onkey(fun = r_paddle.go_up, key ="Up")
screen.onkey(fun = r_paddle.go_down, key ="Down")
screen.onkey(fun = l_paddle.go_up, key ="w")
screen.onkey(fun = l_paddle.go_down, key ="s")

game_is_on = True

while game_is_on:
    screen.update() # updates the screen manually everytime

# It holds the popped up window screen
screen.exitonclick()