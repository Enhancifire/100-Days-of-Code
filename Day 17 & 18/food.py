from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.goto(random.randint(-width/2 + 40,width/2 - 40), random.randint(-height/2 + 40, height/2 - 40))

    def moveYoAss(self):
        self.goto(random.randint(-self.width/2 + 40,self.width/2 - 40), random.randint(-self.height/2 + 40, self.height/2 - 40))

