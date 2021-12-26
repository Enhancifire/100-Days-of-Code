from turtle import Turtle, Screen
import random

t = Turtle()
t.pensize(10)
t.speed(0)
screen = Screen()
screen.colormode(255)

def dot():
    toBeOrNotToBe = random.randint(0, 10)
    if toBeOrNotToBe % 7 == 0:
        pass

    else:
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        t.pencolor(color)
        t.circle(1)

def move(x, y):
    
    t.penup()
    t.setpos(x, y)
    t.pendown()
    dot()

def main():
    for i in range(-145, 145, 30):
        for j in range(-145, 145, 30):
            move(i, j)

    t.penup()
    t.setpos(0, 0)
    

main()
screen.exitonclick()