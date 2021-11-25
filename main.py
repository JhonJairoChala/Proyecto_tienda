
from os import remove

#Lista en la cuàl se van a almacenar todos los clientes que se creen
clientes=[]

#Funciòn para agregar un nuevo cliente
def crear_cliente():
    nombreCompleto=input("Ingrese el nombre completo del cliente: ")
    numeroCelular=int(input("Ingrese el numero de telefono del cliente: "))
    saldo=float(input("Ingrese el saldo del cliente:"))
    clientes.append(nombreCompleto)
    clientes.append(numeroCelular)
    clientes.append(saldo)


#Funciòn para buscar los datos de un cliente
def buscar_cliente():
    numeroCelular = int(input("Ingrese el numero celular del cliente que quiere buscar: "))
    if numeroCelular in clientes:
            print("Estos son los datos del cliente que ha buscado: ",clientes) 
    else:
        print("El cliente no existe")


#Funciòn para actualizar los datos de un cliente
def actualizar_cliente():
    existe = False
    nombreCompleto = input("Ingrese el nombre completo del cliente: ")
    
    for i in range(len(clientes)):
        if (nombreCompleto == clientes[0]):
            existe = True
            pos = i
            break

    if (existe):    
        #La sentencia del nos ayuda a eliminar un elemento de una lista con la posiciòn que le indiquemos
        del clientes[0]
        nuevoNombreCompleto = input("Ingrese los nombres completos del cliente: ")
        clientes.insert(0,nuevoNombreCompleto)
        del clientes[1]
        numeroCelular = int(input("Ingrese el numero celular del cliente: "))
        clientes.insert(1,numeroCelular)
        opcionSaldo = input("Ingrese si va a sumar o restar en el saldo del cliente: ")
        if opcionSaldo == "sumar":
            del clientes[2]
            montoASumar = int(input("Ingrese el monto a sumar en el saldo por el cliente: "))
            saldo = float(input("Ingrese el saldo del cliente: "))
            saldoActual = (montoASumar+saldo)
            print("Este es el saldo actual del cliente: ",saldoActual)
            clientes.insert(2,saldoActual)
            print("Estos son los datos actualizados del cliente: ",clientes)

        elif opcionSaldo == "restar":
            del clientes[2]
            montoASumar = int(input("Ingrese el abono en el saldo por el cliente: "))
            saldo = float(input("Ingrese el saldo actual  del cliente: "))
            saldoActual = (montoASumar-saldo)
            print("Este es el saldo actual del cliente: ",saldoActual)
            clientes.insert(2,saldoActual)
            print("Estos son los datos del cliente: ", clientes)
    else:
        print("El cliente no existe")

#Funciòn de menù para dar a elegir una serie de opciones disponibles para que el usuario pueda usar
def menu():
    print("Opcion 1 para crear un cliente: ")
    print("Opcion 2 para actualizar un cliente: ")
    print("Opcion 3 para buscar un cliente: ")
    try:
        opcion = int(input("Ingrese la opcion: "))
        if opcion == 1:
            crear_cliente()
        elif opcion == 2:
            actualizar_cliente()
        elif opcion == 3:
            buscar_cliente()
        else:
            print("La opcion no es valida")
    except ValueError:
        print("Ocurrio un error, lo que ingreso no es un nùmero o no se encuentra dentro del rango definido del programa")
    menu()
menu()