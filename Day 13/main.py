from turtle import *
import random

t = Turtle()
t.color("coral")

# t.circle(100)
t.left(72)

for i in range (0,5):
    t.fd(80)
    t.left(144)

t.right(144)

for i in range (0,5):
    t.fd(80)
    t.right(144)

t.left(72)
t.right(18)

for i in range (0,5):
    t.fd(80)
    t.left(144)

for i in range (0,5):
    t.back(80)
    t.left(144)


my_screen = Screen()

my_screen.canvheight = 300
my_screen.canvwidth = 300

my_screen.exitonclick()