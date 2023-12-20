from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template ("home.html.jinja")

@app.route('/ping')
def ping():
    return"<h1>pong</h1>"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello {name}"