from flask import Flask
from flask import render_template
from flask import request
import sqlite3

app= Flask(__name__) ## we telling that this is the app. That is global

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/bracelet")
def bracelet():
    return render_template("braceletPDP.html")
@app.route("/chart")
def chart():
    return render_template("chart.html")

@app.route("/comingsoon")
def comingsoon():
    return render_template("comingSoon.html")

@app.route("/earring")
def earring():
    return render_template("earringsPDP.html")

@app.route("/necklace")
def necklace():
    return render_template("necklacePDP.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/rings")
def rings():
    return render_template("ringsPDP.html")