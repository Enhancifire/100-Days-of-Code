from turtle import Turtle, Screen
import random

colors = ["red", "green", "blue", "yellow", "cyan", "coral", "gold", "orange", "blue violet", "medium spring green"]

t = Turtle()
t.pensize(5)
screen = Screen()


def choice(number):
    if number == 0:
        t.left(90)
        t.fd(40)
        
    if number == 1:
        t.right(90)
        t.fd(40)

    if number == 2:
        t.left(90)
        t.bk(40)

    if number == 3:
        t.right(90)
        t.bk(40)
     

for i in range(200):
    t.color(random.choice(colors))
    num = random.randint(0,1)
    choice(num)

screen.exitonclick()
