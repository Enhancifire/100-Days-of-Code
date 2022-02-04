from turtle import Turtle, Screen
import turtle
import os
import pandas as pd

FONT = ("Courier", 15, "normal")

def main():
    screen = Screen()
    screen.title("State Game")

    file_location = "blank_states_img.gif"
    file_path = os.path.join("Day 23",file_location)
    screen.addshape(file_path)
    turtle.shape(file_path)

    data = pd.read_csv(os.path.join("Day 23","50_states.csv"))

    stateList = data.state.to_list()
    
    stateDrawer = Turtle()
    stateDrawer.penup()
    stateDrawer.hideturtle()
    
    guessedStateList = []

    score = len(guessedStateList)

    def drawstate(state, answer_state):
        
        stateDrawer.goto(int(state.x), int(state.y))
        
        stateDrawer.write(answer_state, align="center", font=FONT)
        return

    def checkName():
        answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="Guess the name of the state")
        if answer_state == "exit":
            return True
        answer_state = answer_state.capitalize()
        if answer_state in guessedStateList:
            return 

        if answer_state in stateList:
            guessedStateList.append(answer_state)
            statedata = data[data.state == answer_state]
            drawstate(statedata, answer_state)
        
            return 



    while len(guessedStateList) != 50:
        tof = checkName()
        if tof:
            break

        score = len(guessedStateList)
        
    screen.exitonclick()
    

if __name__ == "__main__":
    main()
