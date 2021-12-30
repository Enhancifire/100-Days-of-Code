from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.score = 0
        self.WIDTH = width
        self.HEIGHT = height
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, self.HEIGHT/2 - 40)
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"), align="center")

    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 24, "normal"), align="center")
