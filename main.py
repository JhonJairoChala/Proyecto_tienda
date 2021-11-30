from flask import Flask

from flask import Flask, render_template, request, redirect, flash, sessions


from controlador.controlador_general import insertar_Cliente
from controlador.controlador_general import obtener_Cliente
from controlador.controlador_general import actualizar_Cliente
from controlador import controlador_general



app = Flask(__name__)

#Funcion para redireccionar al formulario para agregar un cliente
@app.route("/agregar_cliente")
def formulario_agregar_cliente():
        return render_template("formulario_Cliente.html")

#Funcion para guardar el cliente con los datos datos en el formulario
@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
        nombresCompleto = request.form["nombresCompleto"]
        numeroCelular = request.form["numeroCelular"]
        saldo = request.form["saldo"]
        insertar_Cliente(nombresCompleto, numeroCelular, saldo)
        return redirect("/")

#Funcion para redireccionar al formulario para editar/actualizar cliente
@app.route("/formulario_editar_cliente/<int:numeroCelular>")
def editar_cliente(numeroCelular):
        cliente = obtener_Cliente(numeroCelular)
        return render_template("editar_Cliente.html", cliente=cliente)

#Funcion para actualizar al cliente con los datos dados en el formulario
@app.route("/actualizar_Cliente", methods=["POST"])
def actualizar_cliente(): 
        numeroCelular = request.form["numeroCelular"]
        nombresCompleto = request.form["nombresCompleto"]
        saldo = request.form["saldo"]
        actualizar_Cliente(nombresCompleto, numeroCelular, saldo)
        return redirect("/")

#Funcion para redireccionar al formulario de obtener cliente
@app.route("/formulario_obtener_cliente/<int:numeroCelular>")
def buscar_cliente(numeroCelular):
    cliente = obtener_Cliente(numeroCelular)
    return render_template("buscar_Cliente.html", cliente = cliente)

#Funcion para buscar el cliente y obtener sus datos
@app.route("obtener_Cliente", methods=["POST"])
def obtener_Cliente():
    numeroCelular = request.form["numeroCelular"]
    obtener_Cliente(numeroCelular)
    return redirect("/")

if __name__ == "__main__":
    app.run(port=8000, debug=True)


