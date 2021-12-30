from turtle import Turtle, Screen

t = Turtle()
t.color("red")

for _ in range(15):
    t.fd(10)
    t.penup()
    t.fd(10)
    t.pendown()

screen = Screen()
screen.exitonclick()