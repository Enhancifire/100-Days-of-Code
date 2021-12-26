from turtle import Screen
from snake_model import Snake
from food import Food
from scoreboard import ScoreBoard
import time

HEIGHT = 600
WIDTH = 600

score = 0

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title(f"Snake Adventure! {score}")
screen.tracer(0)


snake = Snake(WIDTH, HEIGHT)
food = Food(WIDTH, HEIGHT)
scoreboard = ScoreBoard(WIDTH, HEIGHT)

screen.update()
gameOn = True


while gameOn:
    screen.update()
    time.sleep(0.1)

    snake.move()
    outofbound = snake.checkOutOfBounds()
    bodybashed = snake.bodyCollision()
    
    if outofbound:
        print("You hit the wall! Game Over!")
        break
    else:
        pass

    if bodybashed:
        print("You hit yourself! Game Over!")
        break
    else:
        pass

    
    head = snake.returnHead()
    if head.distance(food) < 15:
        
        scoreboard.updateScore()
        food.moveYoAss()
        snake.addSnake()


    screen.listen()
    screen.onkey(key="w", fun=snake.up)
    screen.onkey(key="a", fun=snake.left)
    screen.onkey(key="s", fun=snake.down)
    screen.onkey(key="d", fun=snake.right)
 

screen.exitonclick()