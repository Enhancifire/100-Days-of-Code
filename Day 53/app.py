from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

app.secret_key = "secret"
Bootstrap(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(420), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<{self.title}>'

class BookForm(FlaskForm):
    name = StringField("Book Name")
    author = StringField("Book Author")
    rating = StringField("Rating")
    submit = SubmitField("Add")

class EditForm(FlaskForm):
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Confirm Edit")

class DeleteIt(FlaskForm):
    submit = SubmitField("Delete")

@app.route('/')
def index():
    all_books = db.session.query(Book).all()

    return render_template('index.html', books = all_books, len=len(all_books))

@app.route('/add', methods=["GET", "POST"])
def add():
    bookform = BookForm()
    if bookform.validate_on_submit():
        book = Book(
                title=bookform.name.data,
                author=bookform.author.data,
                rating=float(bookform.rating.data),
                )

        db.session.add(book)
        db.session.commit()
        return redirect('/')
    return render_template('add.html', form=bookform)

@app.route('/edit/<int:id>', methods=["GET", "POST"])
def edit(id):
    edit = EditForm()
    book = Book.query.get(id)
    if edit.validate_on_submit():
        book.rating = float(edit.rating.data)
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', id=id, form=edit, book=book)

@app.route('/delete/<int:id>', methods=["GET", "POST"])
def delete(id):
    book = Book.query.filter_by(id=id).first()
    form = DeleteIt()
    if form.validate_on_submit():
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return redirect('/')
    return render_template('delete.html', id=id, book=book, form=form)

if __name__ == '__main__':
        app.run(debug=True)
