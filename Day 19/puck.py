from turtle import Turtle, Screen
import random
import time

class Puck(Turtle):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.movecounter = 0
        

        # self.setheading(random.randint(0, 360))
        self.setheading(300)

        self.penup()

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.setposition(x, y)
        

    def wallbounce(self):
        len = self.height / 2
        y = self.ycor()
        if (len - (y + 10)) <= 0:
            self.bounceWall()

        if ((-len) - (y - 10)) >= 0:
            self.bounceWall()

    def wallCollide(self):
        len = self.width / 2
        x = self.xcor()

        if (len - (x + 10)) <= 15:
            self.goto(0,0)
            self.setheading(random.randint(0, 360))
            self.movecounter = 0
            return 1

        elif (-len - (x - 10)) >= 0:
            self.goto(0,0)
            self.setheading(random.randint(0, 360))
            self.movecounter = 0
            return 2

    def speed(self):
        self.movecounter += 1
        if self.movecounter == 2:
            self.x_move += 3
            self.y_move += 3

    def bounceWall(self):
        self.y_move *= -1

    def bouncePlayer(self):
        self.x_move *= -1
        self.speed()

    