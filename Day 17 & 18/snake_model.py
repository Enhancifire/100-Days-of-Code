from turtle import Turtle
import time

MOVEDISTANCE = 20

class Snake:

    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height
        self.snake = []
        startPos = [(0, 0), (-20, 0), (-40, 0)]

        for i in range(0,3):
            t = Turtle("square")
            t.color("white")
            t.penup()
            
            t.setpos(startPos[i])
            
            self.snake.append(t)
        

    def addSnake(self):
        t = Turtle("square")
        t.color("white")
        t.penup()
        
        t.setpos(self.snake[len(self.snake)-1].xcor() - 20, self.snake[len(self.snake)-1].ycor(),)
        
        self.snake.append(t)


    def move(self):
        for part in range(len(self.snake) - 1 , 0, -1):
                lastPartx = self.snake[part - 1].xcor()
                lastParty = self.snake[part - 1].ycor()
                lastPartHeading = self.snake[part - 1].heading()
                
                self.snake[part].goto(lastPartx, lastParty)
                self.snake[part].setheading(lastPartHeading)
            
        self.snake[0].fd(MOVEDISTANCE)


    def up(self):
        if self.snake[0].heading() == 270:
            pass
        else:
            self.snake[0].setheading(90)


    def down(self):
        if self.snake[0].heading() == 90:
            pass
        else:
            self.snake[0].setheading(270)


    def left(self):
        if self.snake[0].heading() == 0:
            pass
        else:
            self.snake[0].setheading(180)


    def right(self):
        if self.snake[0].heading() == 180:
            pass
        else:
            self.snake[0].setheading(0)


    def checkOutOfBounds(self):
        if self.snake[0].xcor() >= self.WIDTH/2 or self.snake[0].xcor() <= -self.WIDTH/2:
            return True
        
        elif self.snake[0].ycor() >= self.HEIGHT/2 or self.snake[0].ycor() <= -self.HEIGHT/2:
            return True

        else:
            return False


    def bodyCollision(self):
        headpos = self.snake[0].position()

        for segment in range(1, len(self.snake)):
            if headpos == self.snake[segment].position():
                return True
            
            else:
                continue


    def returnHead(self):
        return self.snake[0]
