import random
from turtle import Turtle

INITIAL_SPEED = 0.1

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.goto(position)
        self.penup()
        self.speed(10)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = INITIAL_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.85

    def next_round(self):
        self.goto(0, 0)
        self.move_speed = INITIAL_SPEED
        self.x_move *= -1

