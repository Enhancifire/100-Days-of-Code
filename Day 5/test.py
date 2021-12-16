import random

choice = {
        0: "Rock",
        1: "Paper",
        2: "Scissors",
        }

print("Rock Paper Scissor time!!!")
playerChoice = int(input("Please enter 0 for Rock, 1 for Paper and 2 for Scissor: "))
compChoice = random.randint(0,2)
print(f"Computer chose {choice[compChoice]}")

if compChoice == playerChoice:
    print("It's a Tie!")

elif playerChoice == 0:

    if compChoice == 1:
        print("You Lose!")

    if compChoice == 2:
        print("You Win!")

elif playerChoice == 1:

    if compChoice == 0:
        print("You Win!")

    if compChoice == 2:
        print("You Lose!")

elif playerChoice == 2:

    if compChoice == 0:
        print("You Lose!")

    if compChoice == 1:
        print("You Win!")
