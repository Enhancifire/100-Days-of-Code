from turtle import Turtle, Screen, colormode
import random

t = Turtle()
screen = Screen()
t.speed(0)
colormode(255)
for i in range(180):
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.pencolor(color)
    t.circle(100)
    t.left(2)

screen.exitonclick()