from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user_name = "goodjob"
    
    return render_template("home.html.jinja", user_name = user_name)

@app.route('/ping')
def bub():
    return "<h1> Pong <h1>"


@app.route('/hello/<name>')
def hello(name):
    # return "Hello" + name

    return f"<h1> Hello {name} <h1>"
