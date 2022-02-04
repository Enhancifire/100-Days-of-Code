from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    res = requests.get('https://api.npoint.io/0262a6a112e4b7f491be')
    data = res.json()
    return render_template("index.html", posts=data)


@app.route('/post/<int:num>')
def post(num):
    res = requests.get('https://api.npoint.io/0262a6a112e4b7f491be')
    data = res.json()
    blog = data[num]
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
