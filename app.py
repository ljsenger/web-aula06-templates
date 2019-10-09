from flask import Flask, render_template, request, json, url_for, redirect, make_response
from flask_bootstrap import Bootstrap


#modelos={"0": "pegasus", "1": "vintage", "2": "sport"}
modelos = { "0":  {"nome": "pegasus", "preco": 500, "promocao": False},
            "1":  {"nome": "vintage", "preco": 1500, "promocao": False},
            "2":  {"nome": "sport",   "preco": 1500, "promocao": True},
            "3":  {"nome": "eco",     "preco": 759, "promocao": True}
}


app = Flask("app")
bootstrap = Bootstrap(app)
u = None

@app.route("/")
def index():
    
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    
    return render_template("index.html", name=name, u=u)

@app.route("/modelos")
def produtos():
    return render_template("produtos.html", m=modelos)

@app.route("/promocoes")
def promocoes():
    return render_template("promocoes.html", m=modelos)    

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

@app.route('/login', methods=['POST', 'GET'])
def entre():
    
    if request.method == 'POST':
        setUser(request.form['email'])
        return render_template("index.html", name=u, u=u)
    else:
        return render_template("login.html")
    return render_template("index.html", name=u, u=u)    

def setUser(user):
    global u 
    u = user

def getUser():
    return u

@app.context_processor
def contextProc():
    return dict(getUser=getUser)

if __name__ == "__main__":
    app.run(debug=True)

