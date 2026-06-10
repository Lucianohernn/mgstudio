import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# rutas
@app.route("/")
def inicio():
    return render_template("index.html")




@app.route("/admin/login", methods=["GET", "POST"]) #methods indica los parametro(solicitudes http)
def admin_login(): #funcion

    if request.method == "POST":

        usuario = request.form["usuario"]
        password = request.form["password"]

        conexion = sqlite3.connect("mgstudio.db")
        cursor = conexion.cursor()

        cursor.execute(
            "SELECT * FROM administradores WHERE usuario = ? AND password = ?",
            (usuario, password)
        )

        administrador = cursor.fetchone()

        conexion.close()

        if administrador: #tiene dato?
            return "<h1>Login correcto</h1>"
        else:
            return "<h1>Usuario o contraseña incorrectos</h1>"

    return render_template("admin_login.html")

if __name__ == "__main__":
    app.run(debug=True)