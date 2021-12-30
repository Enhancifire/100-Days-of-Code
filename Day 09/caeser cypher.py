initText = '''
░█████╗░░█████╗░███████╗░██████╗███████╗██████╗░  ░█████╗░██╗░░░██╗██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗  ██╔══██╗╚██╗░██╔╝██╔══██╗██║░░██║██╔════╝██╔══██╗
██║░░╚═╝███████║█████╗░░╚█████╗░█████╗░░██████╔╝  ██║░░╚═╝░╚████╔╝░██████╔╝███████║█████╗░░██████╔╝
██║░░██╗██╔══██║██╔══╝░░░╚═══██╗██╔══╝░░██╔══██╗  ██║░░██╗░░╚██╔╝░░██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
╚█████╔╝██║░░██║███████╗██████╔╝███████╗██║░░██║  ╚█████╔╝░░░██║░░░██║░░░░░██║░░██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝  ░╚════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encodeOrDecode():
    res = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if res == 'encode':
        return 0
    elif res == 'decode':
        return 1
    else:
        return 2


def shouldContinue():
    res = input("Type 'yes' to go again. Otherwise, type 'no'.\n")

    if res == 'yes':
        return 0
    elif res == 'no':
        return 1
    else:
        return 2


def caeser(text, shiftValue, direction):
    finalText = ""

    for letter in text:
        index = alphabet.index(letter)

        if direction == 0:
            newPosition = index + shiftValue
        elif direction == 1:
            newPosition = index - shiftValue

        finalText += alphabet[newPosition]

    print(f"The result is {finalText}")


def main():
    print(initText)

    canContinue = True
    while canContinue:
        res = encodeOrDecode()
        text = input("Type your message:\n").lower()
        shiftValue = int(input("Type the shift number:\n"))

        caeser(text, shiftValue, res)
        
        contRes = shouldContinue()
        if contRes == 0:
            continue

        if contRes == 1:
            canContinue = False
    

main()