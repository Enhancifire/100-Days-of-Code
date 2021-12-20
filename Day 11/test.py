import random

NUMBER = random.randint(0,100)

def checkNum(number):
    if number > NUMBER:
        return 0

    elif number < NUMBER:
        return 1

    elif number == NUMBER:
        return 2
    

def easyOrHard():
    print("Do you want to play it easy or hard?")
    difficulty = input("'Easy' or 'Hard': ").lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5

    else:
        print("Invalid Choice")
        return easyOrHard()

def isNotZero(number):
    if number == 0:
        return False
    else:
        return True


def main():
    chances = easyOrHard()

    cont = isNotZero(chances)
    
    print(f"You have {chances} chances.")

    while cont:
        cont = isNotZero(chances)
        number = int(input("Please enter a number: "))
        numcheck = checkNum(number)
        
        if numcheck == 0:
            print(f"{number} is too high!")
            chances -= 1
        elif numcheck == 1:
            print(f"{number} is too low!")
            chances -= 1
        elif numcheck == 2:
            print("You guessed correctly!!")
            break
        print(f"You have {chances} chances remaining")

    print("Would you like to play again?")
    yn = input("y/N: ").lower()
    if yn == "y":
        main()
    elif yn == "n":
        pass

main()