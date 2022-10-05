from psycopg2 import connect
 
HOST = 'ec2-44-205-63-142.compute-1.amazonaws.com'
PUERTO = 5432
BD = 'dehf0nblh7etqm'
USUARIO = 'skqpanzywbkvkc'
PASS = 'bfcbf923ff78451b63dd5165d478226b1147b8f3ab7a366fe784e31603edde78'

def EstablecerConexion():
    try:
        conexion = connect(host=HOST, port=PUERTO, dbname=BD,user=USUARIO, password=PASS)
    except ConnectionError:
        print("Error de conexión")
    return conexion
