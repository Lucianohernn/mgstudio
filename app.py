import sqlite3
from flask import (Flask, render_template, request, redirect)

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
            return redirect("/admin/dashboard")
        else:
            return "<h1>Usuario o contraseña incorrectos</h1>"

    return render_template("admin_login.html")


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin_dashboard.html")


@app.route("/admin/clientes")
def admin_clientes():
    
    conexion = sqlite3.connect("mgstudio.db")
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, dni, telefono
        FROM clientes
        ORDER BY nombre
    """)

    clientes = cursor.fetchall()

    conexion.close()

    return render_template(
        "admin_clientes.html",
        clientes=clientes
    )

@app.route("/admin/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():
    
    if request.method == "POST":

        nombre = request.form["nombre"]
        dni = request.form["dni"]
        telefono = request.form["telefono"]
        fecha_nacimiento = request.form["fecha_nacimiento"]

        conexion = sqlite3.connect("mgstudio.db")
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO clientes
            (nombre, dni, telefono, fecha_nacimiento)
            VALUES (?, ?, ?, ?)
        """, (
            nombre,
            dni,
            telefono,
            fecha_nacimiento
        ))

        conexion.commit()
        conexion.close()

        return redirect("/admin/clientes")
    
    return render_template("nuevo_cliente.html")

if __name__ == "__main__":
    app.run(debug=True)