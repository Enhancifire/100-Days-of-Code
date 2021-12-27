from turtle import Turtle, Screen
import random
import time
from puck import Puck
from player import Player
from score import ScoreBoard

HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Ping Pong!!")
screen.tracer(0)

puck = Puck(WIDTH, HEIGHT)

PLAYER1X = 350
PLAYER2X = -350

player1 = Player(PLAYER1X, width=WIDTH, height=HEIGHT)
player2 = Player(PLAYER2X, width=WIDTH, height=HEIGHT)
score = ScoreBoard(WIDTH, HEIGHT)

screen.update()

while True:
    puck.move()
    puck.wallbounce()
    puck.wallCollide()
    screen.listen()
    screen.onkey(key="w", fun=player1.moveUp)
    screen.onkey(key="s", fun=player1.moveDown)
    screen.onkey(key="i", fun=player2.moveUp)
    screen.onkey(key="k", fun=player2.moveDown)

    

    if puck.xcor() > PLAYER1X - 2 and puck.distance(player1) < 50:
        head = puck.heading()
        print(head)
        puck.bounce()
        puck.goto(puck.xcor()-20, puck.ycor())
        puck.move()

    screen.update()
    
    time.sleep(0.1)



screen.exitonclick()