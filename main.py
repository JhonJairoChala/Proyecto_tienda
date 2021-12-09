from flask import Flask
from os import close
import os
import re

from flask.helpers import url_for
from flask.templating import render_template_string

from flask import Flask, render_template, request, redirect, flash, sessions


from controlador.controlador_general import insertar_Cliente, listar_Cliente
from controlador.controlador_general import obtener_Cliente
from controlador.controlador_general import actualizar_Cliente
from controlador.controlador_general import listar_Cliente
from controlador import controlador_general


app = Flask(__name__)

@app.route("/")
def principal():
        return render_template('index.html')

#Funcion para redireccionar al formulario para agregar un cliente
@app.route("/agregar_cliente")
def agregar_cliente():
        return render_template('crear.html')

#Funcion para guardar el cliente con los datos datos en el formulario
@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
        nombresCompleto = request.form["nombresCompleto"]
        numeroCelular = request.form["numeroCelular"]
        saldo = request.form["saldo"]
        insertar_Cliente(nombresCompleto, numeroCelular, saldo)
        return redirect("/")

#Funcion para redireccionar al formulario para editar/actualizar cliente
@app.route("/formulario_editar_cliente")
def editar_cliente(numeroCelular):
        Cliente = obtener_Cliente(numeroCelular)
        return render_template('actualizar.html', cliente=Cliente)

#Funcion para actualizar al cliente con los datos dados en el formulario
@app.route("/actualizar_Cliente", methods=["POST"])
def actualizar_cliente(): 
        numeroCelular = request.form["numeroCelular"]
        nombresCompleto = request.form["nombresCompleto"]
        saldo = request.form["saldo"]
        actualizar_Cliente(nombresCompleto, numeroCelular, saldo)
        return redirect("/")

#Funcion para redireccionar al formulario de obtener cliente
@app.route("/formulario_obtener_cliente")
def buscar_cliente(numeroCelular):
    cliente = obtener_Cliente(numeroCelular)
    return render_template('buscar.html', cliente = cliente)

#Funcion para buscar el cliente y obtener sus datos
@app.route("/obtener_Cliente", methods=["POST"])
def obtener_Cliente():
        numeroCelular = request.form["numeroCelular"]
        obtener_Cliente(numeroCelular)
        return redirect("/")


@app.route("/menu_General")
def clientes():
    clientes = listar_Cliente()
    return render_template("/", cliente=clientes)

if __name__ == "__main__":
    app.run(port=7000, debug=True)


