from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/1")
def pagina1():
    return render_template("1.html")

@app.route("/2")
def pagina2():
    return render_template("2.html")

@app.route("/3")
def pagina3():
    return render_template("3.html")

@app.route("/4")
def pagina4():
    return render_template("4.html")

@app.route("/5")
def pagina5():
    return render_template("5.html")

@app.route("/6")
def pagina6():
    return render_template("6.html")

@app.route("/7")
def pagina7():
    return render_template("7.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(debug=True)
