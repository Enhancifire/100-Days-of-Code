from turtle import Turtle, Screen

t = Turtle()
t.speed(0)
t.color("coral")

for i in range(0, 4):
    t.circle(90)
    t.left(90)

t.color("cyan")
for i in range(0, 36):
    t.circle(50)
    t.left(10)


my_screen = Screen()

my_screen.canvheight = 300
my_screen.canvwidth = 300

my_screen.exitonclick()