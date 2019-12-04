from flask import Flask, render_template, redirect, request, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)

@app.route('/')
def eight_eight():
    return render_template("eight_eight.html")

@app.route('/4')
def eight_four():
    return render_template("eight_four.html")

@app.route('/<x>/<y>')
def random(x,y):
    return render_template("random_board.html", x=int(x), y=int(y))

if __name__ == "__main__":
    app.run(debug=True)