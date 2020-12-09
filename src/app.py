import os
import sys
from flask import Flask, render_template, request, redirect
from Photomath import *

app = Flask(__name__)
app.config["IMAGE_UPLOADS"] = "./uploads"

global photomath

@app.route("/", methods=["GET", "POST"])
def upload_image():
    result = ''
    expression = ''
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            path_to_image = os.path.join(app.config["IMAGE_UPLOADS"], image.filename)
            image.save(path_to_image)
            print("Image saved")
            result = photomath.calculate(path_to_image)
            expression = photomath.expression + ' = '
    return render_template("upload_image.html", result=result, expression=expression)

if __name__ == "__main__":
    character_detector = CharacterDetector()
    character_classifier = CharacterClassifier()
    solver = Solver()
    photomath = Photomath(character_detector, character_classifier, solver)

    #Train or load model
    path = str(sys.argv[2])
    if str(sys.argv[1]) == '1':
        photomath.train_model(path)
    else:
        photomath.load_classification_model(path)

    app.run()