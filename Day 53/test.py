from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(420), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.title

@app.route('/')
def index():
    return f"{db.session.query(Book).all()}"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
