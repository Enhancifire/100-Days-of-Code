from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

loginMan = LoginManager()
loginMan.init_app(app)

@loginMan.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        return f"User: {self.name}"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        hashed = generate_password_hash(request.form.get('password'),
                method='pbkdf2:sha256',
                salt_length=8)

        name = request.form.get('name')
        email = request.form.get('email')

        newUser = User(
                name= name,
                email=email,
                password=hashed,
                )
        db.session.add(newUser)
        db.session.commit()

        load_user(newUser)

        return redirect(url_for('secrets'))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/secrets/<user>')
@login_required
def secrets(user):
    return render_template("secrets.html", user=current_user.name)


@app.route('/download')
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf', as_attachment=False)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
