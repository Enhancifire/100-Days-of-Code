from flask import Flask, redirect, render_template, request, url_for
import os
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename
from wtforms import StringField, SubmitField
import numpy as np
import cv2
from convert import process

app = Flask(__name__)
app.config["SECRET_KEY"] = "laskdjf"
app.config["UPLOAD_FOLDER"] = "uploads"


class FileForm(FlaskForm):
    file = FileField("Select Image")


@app.route('/', methods=['GET', 'POST'])
def index():

    form = FileForm()

    if form.validate_on_submit():

        filename = secure_filename(form.file.data.filename)
        form.file.data.save(os.path.join(
            app.config["UPLOAD_FOLDER"], filename))

        image = cv2.imread(f"{app.config['UPLOAD_FOLDER']}/{filename}")
        data = process(image)

        print(data)

        return render_template("colors.html", colorList=data)

    return render_template("index.html", form=form)


def convertColors(data):
    print(data.shape)


if __name__ == "__main__":
    app.run(debug=True)
