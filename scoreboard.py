from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(100,270)
        self.write(arg=f"Score = {self.right_score}", align=ALIGNMENT, font=FONT)
        self.goto(-100,270)
        self.write(arg=f"Score = {self.left_score}", align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.right_score +=1
        self.update_score()

    def declare_winner(self):
        if self.left_score > self.right_score:
            winner = 'left'
        else:
            winner = 'right'

        self.goto(0,100)
        self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT)
        self.goto(0, 70)
        self.write(arg=f"{winner} player wins!", align=ALIGNMENT, font=FONT)



    # @staticmethod
    # def declare_winner(player):
    #     winner = Turtle()
    #     winner.color('white')
    #     winner.goto(0, 100)
    #     winner.hideturtle()
    #     winner.write(arg=f" Game Over!\n{player} wins!", align=ALIGNMENT, font=FONT)
