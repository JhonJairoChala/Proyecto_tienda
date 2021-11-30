#Este import sirve para importar la conexion a la base de datos
from bd import obtener_conexion

#Funcion para agregar clientes
def insertar_Cliente(nombresCompleto,numeroCelular,saldo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO tienda.clientes (nombresCompleto,numeroCelular,saldo) VALUES (%s, %s, %s)",(nombresCompleto,numeroCelular,saldo))
    conexion.commit()
    conexion.close()

#Funcion para buscar un cliente y obtener sus datos
def obtener_Cliente(numeroCelular):
    conexion = obtener_conexion()
    cliente = None
    with conexion.cursor() as cursor:
        cursor.execute("SELECT clientes.nombresCompleto as nombresCompleto, clientes.numeroCelular as numeroCelular, clientes.saldo as saldo FROM tienda.clientes WHERE numeroCelular = %s", (numeroCelular,))
        cliente = cursor.fetchone()
    conexion.close()
    return cliente

#Funcion para actualizar un cliente
def actualizar_Cliente(nombresCompleto,numeroCelular,saldo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE clientes SET nombresCompleto = %s, numeroCelular = %s, saldo = %s WHERE numeroCelular = %s",(nombresCompleto,numeroCelular,saldo))
    conexion.commit()
    conexion.close()


