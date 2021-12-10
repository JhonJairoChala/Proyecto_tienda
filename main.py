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

buscar_clientes=[]

@app.route("/")
def principal():
        clientes = listar_Cliente()
        return render_template('index.html', clientes = clientes)

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
def editar_cliente():
        return render_template('actualizar.html')

#Funcion para actualizar al cliente con los datos dados en el formulario
@app.route("/actualizar_Cliente", methods=["POST"])
def actualizar_cliente(): 
        nombresCompleto = request.form["nombresCompleto"]
        numeroCelular = request.form["numeroCelular"]
        saldo = request.form["saldo"]
        actualizar_Cliente(nombresCompleto, numeroCelular, saldo)
        return redirect("/")

#Funcion para redireccionar al formulario de obtener cliente
@app.route("/formulario_obtener_cliente")
def buscar_cliente():
        return render_template('imprimir_buscar.html')

@app.route("/otro")
def otro ():
        return render_template('otro.html',buscar_clientes=buscar_clientes)

@app.route("/cualquiera")
def cualquiera():
        return render_template("imprimir_buscar.html")


@app.route("/imprimir_Datos", methods=["POST"])
def buscar_Cliente_Por_Celular():
        numeroCelular = request.form["numeroCelular"]
        cliente = controlador_general.obtener_Cliente(numeroCelular)
        print ("este es el cliente", cliente)
        buscar_clientes.append(cliente)
        try:
                if numeroCelular == cliente[1]:
                        print ("Entro por a qui")
                        return redirect ('/otro')
                else:
                        return "Error el numero no existe"
        except Exception as error:
                return redirect ("/cualquiera")
if __name__ == "__main__":
    app.run( port=5000, debug=True)


