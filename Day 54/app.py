from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import movieserver

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my-top-movies.db"
db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

apikey = movieserver.connect()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(120))
    img_url = db.Column(db.String(120), nullable=False)


class EditMovie(FlaskForm):
    rating = StringField("Your Rating")
    review = StringField("Review")
    submit = SubmitField("Done")


class AddMovie(FlaskForm):
    name = StringField("Movie Name", validators=[DataRequired()])
    submit = SubmitField("Search")

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating).all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i

    db.session.commit()
    return render_template("index.html", movies=movies)


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    editform = EditMovie()
    movie = Movie.query.get(id)
    if editform.validate_on_submit():
        movie.rating = float(editform.rating.data)
        movie.review = editform.review.data

        db.session.commit()

        return redirect("/")

    return render_template("edit.html", form=editform)


@app.route("/delete/<int:id>")
def delete(id):
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect("/")


@app.route("/add/<int:id>", methods=["GET", "POST"])
def movieAdd(id):
    global apikey
    url = "https://api.themoviedb.org/3/movie/"
    query = f"{url}{id}?api_key={apikey}"

    res = requests.get(query)
    data = res.json()
    name = data["original_title"]
    poster = data["poster_path"]
    desc = data["overview"]
    release_date = data["release_date"].split("-")[0]
    img_base_url = "https://www.themoviedb.org/t/p/w500"
    img = f"{img_base_url}{poster}"

    data = [name, release_date, desc, img]

    newMovie = Movie (
        title=name,
        year= release_date,
        description= desc,
        img_url= img,
    )
    db.session.add(newMovie)
    db.session.commit()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    movieForm = AddMovie()
    if movieForm.validate_on_submit():
        return render_template(
            "select.html", movies=movieserver.search(movieForm.name.data)
        )

    return render_template("add.html", form=movieForm)


if __name__ == "__main__":
    app.run(debug=True)
