from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    
    def __init__(self, ycor, speed):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.goto(280, ycor)
        self.dist = speed
        self.shape("square")
        self.shapesize(stretch_len=2)
        color = random.choice(COLORS)
        self.color(color)
    
    def move(self):
        self.fd(self.dist)

    def incrementSpeed(self):
        self.dist += MOVE_INCREMENT

    def outofBounds(self):
        if self.xcor() < -300:
            return True
        
        else:
            return False



class CarManager:
    
    def __init__(self):
        self.carList = []
        self.carspeed = STARTING_MOVE_DISTANCE

    
    def carCreater(self):
        y = random.randint(-255, 255)
        c = Car(y, self.carspeed)

        self.carList.append(c)

    def carMove(self):
        for car in self.carList:
            car.move()

    def speedIncrease(self):
        for car in self.carList:
            car.incrementSpeed()

    def nextLevel(self):
        self.carlist = []
        self.carspeed += MOVE_INCREMENT

    def crash(self, pos):

        for car in self.carList:
            if car.distance(pos) <= 20:
                return True
                