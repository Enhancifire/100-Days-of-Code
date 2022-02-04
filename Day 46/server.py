from flask import Flask
import random

app = Flask(__name__)

#NUMBER = random.randint(0,100)
NUMBER = 5


def checkNumber(number):
    if number > NUMBER:
        return 0

    elif number < NUMBER:
        return 1

    elif number == NUMBER:
        return 2

def headerDecorator(func):
    def header():
        return f"<h1>{func()}</h1>"
    return header

def winImage(func):
    def header():
        return f'''
    {func()}
    <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">
    '''
    return header

def upImage(func):
    def header():
        return f'''
    {func()}
    <img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">
    '''
    return header

def downImage(func):
    def header():
        return f'''
    {func()}
    <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">
    '''
    return header

@app.route('/')
def numberGuesser():

    return "Number Guessed"


@app.route('/<int:num>')
def game(num):
    number = checkNumber(num)

    @winImage
    @headerDecorator
    def correctGuess():
        return "You got me!"

    @upImage
    @headerDecorator
    def overshoot():
        return "Number is too high!"

    @downImage
    @headerDecorator
    def undershoot():
        return "Number is too low!"

    if number == 0:
        return overshoot()

    elif number == 1:
        return undershoot()

    elif number == 2:
        return correctGuess()


if __name__ == "__main__":
    app.run(debug=True)
