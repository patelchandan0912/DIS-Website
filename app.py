from flask import Flask
from flask import render_template
from flask import Flask, redirect
from flask import request
import sqlite3

app= Flask(__name__) ## we telling that this is the app. That is global

@app.route("/")
def home():
    return render_template("index.html")  ## Home page

@app.route("/about")
def about():
    return render_template("about.html") ## Routing about us page
 
@app.route("/bracelet")
def bracelet():
    return render_template("braceletPDP.html") ## Routingn product landing page
@app.route("/chart")
def chart():
    return render_template("chart.html")  ## routing chart page

@app.route("/comingsoon")
def comingsoon():
    return render_template("comingSoon.html") 

@app.route("/earring")
def earring():
    return render_template("earringsPDP.html") ## Routingn product landing page
@app.route("/chart")

@app.route("/necklace")
def necklace():
    return render_template("necklacePDP.html") ## Routingn product landing page
@app.route("/chart")

@app.route("/product")
def product():
    return render_template("product.html") ## Routingn product landing page
@app.route("/chart")

@app.route("/rings")
def rings():
    return render_template("ringsPDP.html") ## Routingn product landing page
@app.route("/chart")

@app.route("/text1")  ## external font styling link
def text():
    return redirect("https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap")


@app.route("/text2") ## external css for social media icons
def text2(): 
    return redirect("https://cdn.jsdelivr.net/npm/remixicon@2.5.0/fonts/remixicon.css")


@app.route("/lksm")  ## linkdln of the member
def lksm():
    return redirect("https://www.linkedin.com/in/shambhavi-mishra-673a52103/")

@app.route("/gism") ## github of the member
def gism():
    return redirect("https://github.com/Shambhavi1529")

@app.route("/lkrk")
def lkrk():
    return redirect("https://www.linkedin.com/in/raghavkhurana/")

@app.route("/girk")
def girk():
    return redirect("https://github.com/khuranaraghav")

@app.route("/lkck")
def lkck():
    return redirect("https://www.linkedin.com/in/chandni-kumari1231/")

@app.route("/gick")
def gick():
    return redirect("https://github.com/chandnikusf")

@app.route("/lkcp")
def lkcp():
    return redirect("https://www.linkedin.com/in/chandanpatel0912/")

@app.route("/gicp")
def gicp():
    return redirect("https://github.com/patelchandan0912")

@app.route("/chartjs")
def chartjs():
    return redirect("https://cdn.jsdelivr.net/npm/chart.js")

