from flask import Flask, render_template, redirect, request, session, url_for
import sqlite3
import re

app= Flask(__name__)
app.secret_key = 'your secret key'

connection = sqlite3.connect('customers.db')
connection.execute('CREATE TABLE IF NOT EXISTS customers ( id INTEGER PRIMARY KEY, firstname TEXT not null, lastname text not null, phone text not null, email TEXT NOT NULL, password TEXT NOT NULL)')

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


@app.route('/customers')
def customers():
    con = sqlite3.connect("customers.db")
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM customers")

    rows = cur.fetchall()
    return render_template("customers.html", rows=rows)

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
@app.route('/signup', methods=["GET", "POST"])
def signup():
    session.pop('error_message', None)
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        email = request.form['email']
        psw = request.form['psw']
        phone_regex = re.compile(r'^\d{3}-?\d{3}-?\d{4}$')
        if not fname or not lname or not phone or not email or not psw:
            session['error_message'] = 'Please fill all the fields'
        elif not bool(re.match(phone_regex, phone)):
            session['error_message'] = 'please enter a valid phone number'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            session['error_message'] = 'please enter a valid email id'
        elif not len(psw) > 7:
            session['error_message'] = 'Password should contain greater than 7 characters'
        else:
            connection = sqlite3.connect('customers.db')
            curs = connection.cursor()
            curs.execute("Select * from customers where email = ?", (email, ))
            isUserExisted = curs.fetchone()
            if not isUserExisted:
                connection = sqlite3.connect('customers.db')
                curs = connection.cursor()
                curs.execute('Insert into customers (firstname, lastname, phone, email, password) values (?, ?, ?, ?, ?)', (fname, lname, phone, email, psw))
                connection.commit()
                curs.execute("Select * from customers where email = ? and password = ?", (email, psw))
                user = curs.fetchone()
                session['user_info'] = user[0]
                return render_template('index.html', user = user)
            else:
                session['error_message'] = 'User already exists with that email'
    return render_template('signup.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    session.pop('error_message', None)
    if request.method == "POST":
        email = request.form['email']
        password = request.form['psw']
        if not email or not password:
            session['error_message'] = 'Please fill all the fields'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            session['error_message'] = 'please enter a valid email id'
        elif not len(password) > 7:
            session['error_message'] = 'Password should contain greater than 7 characters'
        else:
            connection = sqlite3.connect('customers.db')
            curs = connection.cursor()
            curs.execute("Select * from customers where email = ?", (email, ))
            user = curs.fetchone()
            if not user:
                session['error_message'] = 'Please enter valid email & password'
            else:
                session['user_info'] = user[0] 
                return render_template('index.html', user = user)
    return render_template('login.html')

