# Step01: Create the screen
# Step02: Create and move a paddle
# Step03: Create another paddle
# Step04: Create the ball and make it move
# Step05: Detect collision with wall and bounce
# Step06: Detect collision with paddle
# Step07: Detect when paddle misses
# Step08: Keep score

# Import the necessary modules
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create a screen instance and set its properties
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0) # disable the animation

# create the paddle instances
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create the ball instance
ball = Ball()

# create the scoreboard instance
scoreboard = Scoreboard()

# logic to move the paddles up and down
screen.listen()
screen.onkey(fun = r_paddle.go_up, key ="Up")
screen.onkey(fun = r_paddle.go_down, key ="Down")
screen.onkey(fun = l_paddle.go_up, key ="w")
screen.onkey(fun = l_paddle.go_down, key ="s")

game_is_on = True

while game_is_on:

    """
    So in order to speed up the ball, the key is in how much time we make our game loop sleep.
    Because the shorter that this sleep is, let's say instead of 0.1 second
    let's do 0.01 second. And if we run now, you can see our ball moves a lot faster.
    Let's make it even more extreme and add another zero. So how can we reduce this number by a little bit each time,
    but never make it go into the negative because if this becomes a negative number,
    then we actually get an error over here telling us that the sleep length must be non-negative. 
    In order to do this, we have to figure out a way of making this number a little bit smaller each time.
    """

    time.sleep(ball.move_speed) # delays the loop for a little bit in between each of the updates
    screen.update() # updates the screen manually everytime
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with r_paddle and l_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor()> 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# It holds the popped up window screen
screen.exitonclick()

