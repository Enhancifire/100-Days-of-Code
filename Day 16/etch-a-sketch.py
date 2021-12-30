from turtle import Turtle, Screen

t = Turtle()
screen = Screen()

def moveForward():
    t.fd(10)

def moveBackward():
    t.bk(10)

def turnLeft():
    t.left(10)

def turnRight():
    t.right(10)

def clear():
    t.setposition(0,0)
    t.clear()

screen.listen()
screen.onkey(key="w", fun=moveForward)
screen.onkey(key="s", fun=moveBackward)
screen.onkey(key="a", fun=turnLeft)
screen.onkey(key="d", fun=turnRight)
screen.onkey(key="c", fun=clear)



screen.exitonclick()