from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route('/random', methods=["GET"])
def randroute():
    cafes = db.session.query(Cafe).all()
    cafe = random.choice(cafes)

    return jsonify(cafe= {
        "can_take_calls": cafe.can_take_calls,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        "seats": cafe.seats,
        "has_toilet": cafe.has_toilet,
        "has_wifi": cafe.has_wifi,
        "has_sockets": cafe.has_sockets,
        "coffee_price": cafe.coffee_price,
        }
        )

@app.route('/all', methods=["GET"])
def all():
    cafes = db.session.query(Cafe).all()

    all_cafes = [cafe.to_dict() for cafe in cafes]

    return jsonify(cafes=all_cafes)

@app.route('/search', methods=["GET"])
def search():
    loc = request.args.get('loc')

    try:
        cafe = Cafe.query.filter_by(location=loc).first()

        cafe = cafe.to_dict()

        return jsonify(cafe=cafe)

    except:
        return jsonify(error={
            "Not Found": "Sorry, we do not have a cafe at that location",
            })


## HTTP POST - Create Record
@app.route('/add', methods=["POST"])
def add():
    params = request.args.to_dict()
    try:
        cafe = Cafe(
                name= params["name"],
                map_url= params["map_url"],
                location= params["location"],
                img_url= params["img_url"],
                seats= params["seats"],
                has_toilet= params["has_toilet"],
                has_wifi= params["has_wifi"],
                has_sockets= params["has_sockets"],
                coffee_price= params["coffee_price"],

                )

        db.session.add(cafe)
        db.session.commit()

        return jsonify(success="Cafe added successfully")

    except KeyError:
        return jsonify(error="Parameter missing or misspelled")




## HTTP PUT/PATCH - Update Record
@app.route('/update-record/<int:id>', methods=["PATCH"])
def update(id):
    try:
        newPrice = request.args.get("new_price")

        cafe = Cafe.query.get(id)
        cafe.coffee_price = newPrice
        db.session.commit()

        return jsonify(success="Successfully updated the price")
    except:
        return jsonify(error="Sorry, that Cafe does not exist"), 404

## HTTP DELETE - Delete Record
@app.route('/delete/<int:id>', methods=["DELETE"])
def delete(id):
    try:
        apikey = request.args.get("api-key")
        if apikey == "abcdbbcd":
            cafe = Cafe.query.get(id)
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(success="Entry has been deleted"), 200
        else:
            return jsonify(error="You do not have permission to do this. API KEY invalid"), 400
    except NoResultFound:
        return jsonify(error="Record not found"), 404



if __name__ == '__main__':
    app.run(debug=True)
