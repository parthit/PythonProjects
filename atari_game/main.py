from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(titlestring="Pong")
screen.tracer(0)

l_paddle = Paddle(xcor=-350, ycor=0)
r_paddle = Paddle(xcor= 350, ycor=0)

ball = Ball()
scoreboard = Scoreboard()


screen.listen()



screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Collision with Right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_postion()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_postion()

screen.exitonclick()
