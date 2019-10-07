from flask import Flask, render_template, request, json, url_for, redirect
from flask_bootstrap import Bootstrap

modelos={"0": "pegasus", "1": "vintage", "2": "sport"}

app = Flask("app")
bootstrap = Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("index.html", name=name)

@app.route("/modelos")
def produtos():
    return render_template("produtos.html", m=modelos)

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

if __name__ == "__main__":
    app.run(debug=True)

