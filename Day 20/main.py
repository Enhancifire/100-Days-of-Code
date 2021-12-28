import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score = 1
player = Player()
cars = CarManager()
scoreboard = Scoreboard()
game_is_on = True
carcounter = 0

while game_is_on:
    cars.carMove()
    screen.listen()
    screen.onkey(key="w", fun=player.move)
    carcounter += 1

    if cars.crash(player.position()):
        print("Game Over!!!!!")
        break

    if player.checkWin():
        player.ifWinMove()
        cars.nextLevel()
        score += 1
        scoreboard.scoreIncrease()

    if carcounter == 6:
        cars.carCreater()
        carcounter = 0

    time.sleep(0.1)
    screen.update()

screen.exitonclick()