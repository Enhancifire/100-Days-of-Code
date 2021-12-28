from turtle import Turtle, Screen
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):

        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(-200, 250)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def scoreIncrease(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)