import pymysql 
def obtener_conexion():
	return pymysql.connect(host='localhost',
            user='root',
            password='Sena1234',
            db='tienda')