from flask import Flask
import requests

def get_rate():

app = Flask(__name__)
@app.route("/", methods=["POST"])
def convert():
    amount = float(request.form['amount'])
    rate =