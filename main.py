from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball((0, 0))
score = Score()

screen.listen()
screen.onkeypress(fun=right_paddle.move_up, key='Up')
screen.onkeypress(fun=right_paddle.move_down, key='Down')
screen.onkeypress(fun=left_paddle.move_up, key='w')
screen.onkeypress(fun=left_paddle.move_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_wall()

    if ball.distance(right_paddle) <= 50 and ball.xcor() >= 320 or ball.distance(left_paddle) <= 50 and ball.xcor() <= -320:
        ball.bounce_paddle()

    if ball.xcor() >= 380:
        score.increase_left_score()
        ball.next_round()

    if ball.xcor() <= -380:
        score.increase_right_score()
        ball.next_round()

    if score.left_score >= 10 or score.right_score >= 10:
        score.declare_winner()
        game_is_on = False
screen.exitonclick()
