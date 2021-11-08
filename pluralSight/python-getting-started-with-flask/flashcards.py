from flask import Flask, render_template

from model import db

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        title1="Welcome",
        message1="Message passed as argument",
        emMessage="This is an example flask",
        message2="Message passed as argument",
        link="https://www.pluralsight.com",
        linkTitle="Pluralsight"
    )


@app.route("/card")
def card_view():
    card = db[0]
    return render_template("card.html", card=card)
