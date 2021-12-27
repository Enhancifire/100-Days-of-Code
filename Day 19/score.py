from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, width, height):

        super().__init__()

        self.width = width
        self.height = height

        self.setheading(90)

        self.color("white")

        self.hideturtle()

        self.penup()
        self.goto(0, - self.height / 2)

        for i in range (0, self.height, 20):
            self.pendown()
            self.fd(10)
            self.penup()
            self.fd(10)

        self.goto(0, - self.height / 2 - 80)
        self.write("score1} score2}", font=("Arial", 24, "bold"), align="center")