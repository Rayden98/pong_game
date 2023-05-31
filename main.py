from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

STARTING_POSITIONS = [(350, 0), (-350, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(STARTING_POSITIONS[0])
l_paddle = Paddle(STARTING_POSITIONS[1])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall.
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collisions with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.r_point()

    # Detect collisions with the left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()
        scoreboard.l_point()

    # Detect when the ball goes Out of Bounds
    if ball.xcor() > 390 or ball.xcor() < - 390:
        print("GAME OVER")
        ball.reset_position()


# screen.mainloop()
screen.exitonclick()
