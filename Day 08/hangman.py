import random
import ascii_arts as aart


def checkLetter(letter, word):
    if letter in word:
        letter_position = []
        for i in range(0, len(word)):
            if letter == word[i]:
                letter_position.append(i)
                
        return letter_position
    else:
        return []

def checkBlanks(blank):
    for i in range(0, len(blank)):
        if "_" == blank[i]:
            return True
    return False

def createWord():
    words = ["blank", "plank", "education", "word", "sword"]
    word = random.choice(words)
    return word

def createBlanks(word):
    blank = []

    for i in range(0, len(word)):
        blank += "_"

    return blank

def main():
    life = 5
    aart.printTitle()
    word = createWord()
    blank = createBlanks(word)    

    while life > 0:
        blank_word = ""
        for i in range(0, len(blank)):
            blank_word += f"{blank[i]} "

        print(f"Word = {blank_word}   Lives = {life}\n")

        letter = input("Input Letter: ")
        print("")

        letterCheck = checkLetter(letter, word)
        if len(letterCheck) == 0:
            life -= 1

        else:
            for i in letterCheck:
                blank[i] = letter

        hasblank = checkBlanks(blank)

        if hasblank:
            continue
        else:
            break

    if life > 0:
        aart.win()
    else:
        aart.gameOver()

main()
