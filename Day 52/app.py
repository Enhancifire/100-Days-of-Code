from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Signup')

app.secret_key = "my-secret"

@app.route('/')
def index():
    return render_template("base.html")

@app.route('/login', methods = ["POST", "GET"])
def login():
    loginForm = LoginForm()
    loginForm.validate_on_submit()
    if loginForm.validate_on_submit():
        if loginForm.email.data == "admin@email.com" and loginForm.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=loginForm)

if __name__ == "__main__":
    app.run(debug=True)
