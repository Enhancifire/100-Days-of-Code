import random

blackjack = """
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░███░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░████████████░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░████████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█
█░░▄▀░░░░░░▄▀░░███░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░████████████░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█
█░░▄▀░░██░░▄▀░░███░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░██████████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███
█░░▄▀░░░░░░▄▀░░░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██████████████░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░██████████████░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░███
█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░██████░░░░░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███
█░░▄▀░░████░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░██████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███
█░░▄▀░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░█
█░░▄▀▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀░░█
█░░░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░█
█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
"""


def hitorpass():
    res = input("Type 'y' to get another card, type 'n' to pass: ")
    if res == 'y':
        return True
    
    elif res == 'n':
        return False

def over21(score):
    if score > 21:
        return True
    else:
        return False

def score(cardList):
    score = 0
    for card in cardList:
        score += card

    return score


def deal():
    cardList = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]

    chosenCard = random.choice(cardList)
    return chosenCard
    

def start():
    playerCard = []
    cpuCard = []

    playerCard.append(deal())
    playerCard.append(deal())

    cpuCard.append(deal())
    cpuCard.append(deal())

    return playerCard, cpuCard


def calculate(playerCard, cpuCard):
    playerScore = score(playerCard)
    cpuScore = score(cpuCard)
    print("\nReveal!!!\n")
    print(f"Your cards: {playerCard}, current score: {playerScore}")
    print(f"CPUs cards: {cpuCard}, current score: {cpuScore}")
    print("\n")
    if over21(playerScore):
        print(f"You Lost! Your Score is {playerScore}")
        return

    elif over21(cpuScore):
        print(f"You Win! CPU's Score is {cpuScore}")
        return

    else:
        pass

    if playerScore > cpuScore:
        print("You win!")
    
    else:
        print(f"You lose! CPU Cards: {cpuCard}")


def cpuChoose():
    tf = [True, False]
    res = random.choice(tf)

    if res:
        print("CPU chose to HIT!!!")

    else:
        print("CPU chose to pass")

    return res


def main():
    print(blackjack)
    print()
    playerCard, cpuCard = start()
    playerScore = score(playerCard)
    cpuScore = score(cpuCard)

    print(f"Your cards: {playerCard}, current score: {playerScore}")
    if playerScore == 21:
        print("You have a blackjack! You win!!!")

        return

    elif cpuScore == 21:
        print("Your opponent has a blackjack! You Lost!!!")

        return

    if over21(playerScore):
        print("You lose!")

        return
    
    if over21(cpuScore):
        print("You Win!")

        return
    
    playerRes = hitorpass()
    cpuRes = cpuChoose()

    if playerRes and cpuRes:
        res = True
    else:
        res = False

    while res:
        playerCard.append(deal())
        
        playerScore = score(playerCard)

        print(f"Your cards: {playerCard}, current score: {playerScore}")
        if over21(playerScore):
            break
        else:
            res = hitorpass()
            cpuRes = cpuChoose()

            if playerRes and cpuRes:
                res = True
            else:
                res = False


    calculate(playerCard, cpuCard)


main()