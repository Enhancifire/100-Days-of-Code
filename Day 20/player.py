from turtle import Turtle, Screen


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def checkWin(self):
        pos = self.position()
        if pos[1] == FINISH_LINE_Y:
            return True

    def ifWinMove(self):
        self.goto(STARTING_POSITION)