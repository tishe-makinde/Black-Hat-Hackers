import sys, os

# Get absolute path to backend folder
backend_path = os.path.join(os.path.dirname(__file__), "backend")

# Add it to sys.path if not already there
if backend_path not in sys.path:
    sys.path.append(backend_path)

from main import SourceVerification
import ImageToText

from flask import Flask, render_template, request
from ddgs import DDGS
import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")


"""@app.route("/urlResults", methods=["POST"])
def urlResults():
    url = request.form['url'] 
    print("User entered:", url)
    verify = SourceVerification(url)
    verify.getLink()
    scores = verify.findSimilarLink()

    return scores"""

@app.route("/imgUpload", methods=["POST"])
def imgUpload():
        file = request.form['fileUpload']
        print("User entered:", file)
        verify = ImageToText.finalURL(file)
        print(verify)

        return " " + ImageToText.finalURL(file)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)