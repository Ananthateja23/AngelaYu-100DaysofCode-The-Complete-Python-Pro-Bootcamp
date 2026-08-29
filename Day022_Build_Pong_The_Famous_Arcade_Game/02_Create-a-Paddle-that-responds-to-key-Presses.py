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

# create a screen instance and set its properties
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0) # disable the animation
# Remember that when you turn off the animation,
# you have to manually update the screen and refresh it every single time. 


# create a paddle instance and set properties
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(x = 350, y = 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(x = paddle.xcor(), y = new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(x = paddle.xcor(), y = new_y)

# logic to move the paddle up and down
screen.listen()
screen.onkey(fun = go_up, key ="Up")
screen.onkey(fun = go_down, key ="Down")

game_is_on = True

while game_is_on:
    screen.update() # updates the screen manually everytime

# It holds the popped up window screen
screen.exitonclick()