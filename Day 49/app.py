from flask import Flask
from flask.templating import render_template
import requests

app = Flask(__name__)

@app.route('/blog')
def blog():
    res = requests.get('https://api.npoint.io/c790b4d5cab58020d391')

    blog_data = res.json()

    return render_template("blog.html", posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
