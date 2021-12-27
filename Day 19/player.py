from turtle import Turtle, Screen
import random
import time

class Player(Turtle):

    def __init__(self, posX, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("square")
        self.color("white")
        self.setheading(90)

        self.penup()
        self.setx(posX)

        self.shapesize(stretch_len=5)


    def moveUp(self):
        if self.height / 2 - self.ycor() >= 50:
            self.fd(20)
        
    def moveDown(self):
        if ((- self.height / 2) - self.ycor()) <= -50:
            self.bk(20)

    def returnX(self):
        return self.xcor()