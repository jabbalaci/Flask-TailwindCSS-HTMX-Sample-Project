#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {"name": "world"}
    return render_template("index.html", **context)


@app.route("/clicked")
def fn_clicked():
    return "<b>new text</b>"


if __name__ == "__main__":
    app.run(debug=True)
