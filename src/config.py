from psycopg2 import connect
 
HOST = 'ec2-44-207-133-100.compute-1.amazonaws.com'
PUERTO = 5432
BD = 'd5b6s8gfo43iln'
USUARIO = 'slasirfrbzotmc'
PASS = '470fa5944f7556739700b5296d8959da61d9d8f91e5ddd8d61485f02658458ed'

def EstablecerConexion():
    try:
        conexion = connect(host=HOST, port=PUERTO, dbname=BD,user=USUARIO, password=PASS)
    except ConnectionError:
        print("Error de conexión")
    return conexion
