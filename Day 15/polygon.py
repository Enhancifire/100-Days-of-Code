from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "black", "cyan", "coral", "gold", "orange", "blue violet", "medium spring green"]

t = Turtle()
t.pensize(3)
screen = Screen()
screen.bgcolor("light slate gray")
for i in range(3,11):
    t.color(colors[i-3])

    interiorAngleSum = (2*i - 4) * 90
    interiorAngle = (interiorAngleSum / i)
    print(interiorAngle)

    for j in range(0, i):
        t.fd(100)
        t.right(180 - interiorAngle)



screen.exitonclick()