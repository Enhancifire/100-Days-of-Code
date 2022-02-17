from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField


# Flask Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# Post Add and Edit form
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Index Page
@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


# Showing Post
@app.route("/post/<int:index>")
def show_post(index):
    id = index
    requested_post = BlogPost.query.filter_by(id=id).first()
    return render_template("post.html", post=requested_post)

# Editing Post
@app.route('/edit-post/<int:id>', methods=["GET", "POST"])
def edit_post(id):
    post = BlogPost.query.get(id)

    form = CreatePostForm(
            title=post.title,
            subtitle=post.subtitle,
            author=post.author,
            img_url=post.img_url,
            body=post.body
            )

    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        post.body = form.body.data

        db.session.commit()
        return redirect(url_for('show_post', index=post.id))

    return render_template('make-post.html', form=form, act="Edit")

# Adding New Post
@app.route('/new-post', methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        from datetime import datetime
        x = datetime.now()

        title = form.title.data
        subtitle = form.subtitle.data
        date = x.strftime("%B %d, %Y")
        body = form.body.data
        author = form.author.data
        img_url = form.img_url.data

        newPost = BlogPost(
                title=title,
                subtitle=subtitle,
                date=date,
                body=body,
                author=author,
                img_url=img_url,
                )

        db.session.add(newPost)
        db.session.commit()
        return redirect('/')
    return render_template('make-post.html', form= form, act="Add")

@app.route('/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')


# About Page
@app.route("/about")
def about():
    return render_template("about.html")


# Contact Page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Running the app
if __name__ == "__main__":
    app.run(debug=True)
