#! /usr/bin/env python
from flask import Flask, render_template, request
from handlers.pull import get_pulls

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/pulls')
def pulls():
    state = request.args.get("state")
    return render_template("pulls.j2", pulls=get_pulls(state))


app.run()
