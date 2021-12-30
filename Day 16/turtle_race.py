from turtle import Turtle, Screen
import random

HEIGHT = 768
WIDTH = 1366


screen = Screen()
screen.setup(WIDTH, HEIGHT)


bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
bet = bet.lower()
print("Bet = " + bet)


colors = ["red", "green", "blue", "yellow", "purple",]
positions = [-100, -50, 0, 50, 100]


turtles = []

for i in range(0, 5):
    turtles.append(Turtle())
    turtles[i].color(colors[i])
    turtles[i].shape("turtle")
    turtles[i].penup()
    turtles[i].setpos(-WIDTH/2 + 20, positions[i])


race_goes_on = True


while race_goes_on:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))


    for turtle in turtles:
        if turtle.xcor() >= (WIDTH/2 - 20):
            color = turtle.color()

            if color[0] == bet:
                print("You win!")
            else:
                print(f"You lose! {color[0].upper()} turtle won the race!")

            race_goes_on = False


screen.exitonclick()

    