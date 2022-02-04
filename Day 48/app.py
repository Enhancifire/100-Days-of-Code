import datetime
import requests
from flask import Flask, render_template

app = Flask(__name__)


# get the gender from https://api.genderize.io
def gender(name):

    res = requests.get(f"https://api.genderize.io?name={name}")

    return res.json()["gender"]


def getAge(name):
    res = requests.get(f"https://api.agify.io?name={name}")

    return res.json()["age"]


# get the current year
def get_year():
    return datetime.datetime.now().year


@app.route('/')
def index():

    year = get_year()

    footer = f"Copyright {year} - All Rights Reserved, Built by Faiz Saiyad"
    return render_template('base.html', footer=footer)


@app.route('/guess/<name>')
def ageGuess(name):
    age = getAge(name)
    g = gender(name)

    return render_template('guess.html', name=name.capitalize(), gender=g, age=age)


if __name__ == '__main__':
    app.run(debug=True)
