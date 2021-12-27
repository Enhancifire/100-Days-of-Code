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
        self.speed(10)

        # self.setheading(random.randint(0, 360))
        self.setheading(300)

        self.penup()

    def move(self):
        self.fd(10)

    def wallbounce(self):
        len = self.height / 2
        y = self.ycor()
        if (len - (y + 10)) <= 0:
            self.bounce()

        if ((-len) - (y - 10)) >= 0:
            self.bounce()

    def wallCollide(self):
        len = self.width / 2
        x = self.xcor()

        if (len - (x + 10)) <= 15:
            self.goto(0,0)
            self.setheading(random.randint(0, 360))
            return 1

        elif (-len - (x - 10)) >= 0:
            self.goto(0,0)
            self.setheading(random.randint(0, 360))
            return 2


    def bounce(self):
        
        if self.heading() > 0 and self.heading() < 90:
            self.setheading((self.heading() - (self.heading() * 2)))

        elif self.heading() > 90 and self.heading() < 180:
            head = self.heading() - 90
            self.setheading((self.heading()) + (180 - (head * 2)))

        elif self.heading() > 180 and self.heading() < 270:
            angle = self.heading() - 180
            head = 90 - angle
            self.setheading(self.heading() - (180 - (head * 2)))
        
        elif self.heading() > 270 and self.heading() < 360:
            setangle = 360 - self.heading()
            self.setheading((self.heading() + ((setangle) * 2)))

    