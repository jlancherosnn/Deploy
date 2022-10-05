from flask import Flask, render_template, request, redirect, url_for,flash
from src.config import *
import os

port = int(os.environ.get('PORT', 5000))

con_bd = EstablecerConexion()

app = Flask(__name__)
app.secret_key = 'hay_alguien_aqui_convida_S0Sdd'


@app.route('/')
def index():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM usuari"
    cursor.execute(sql)
    UsuariRegistradas = cursor.fetchall()
    return render_template('index.html', usuarios = UsuariRegistradas)

@app.route('/guardar_usuarios', methods=['POST'])
def agregarUsuarios():
    cursor = con_bd.cursor()
    email = request.form['email']
    password = request.form['password']

    if  email and password:
        sql ="""
            INSERT INTO usuari( email, password)
            VALUES ( %s, %s)
        """
        cursor.execute(sql,(email,password))
        con_bd.commit()
        flash("Registro Guardado Correctamente","info")
        return render_template("registro.html")
    else:
        flash("Registro no sea Guardado Correctamente","error")
        return redirect(url_for('index'))
        
@app.route('/registrar_datos')
def registar_datos():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM producto"
    cursor.execute(sql)
    ProductosRegistradas = cursor.fetchall()
    print(con_bd)
    return render_template('registro.html', productos=ProductosRegistradas)

@app.route('/guardar_productos', methods=['POST'])
def guardar_productos():
    cursor = con_bd.cursor()
    nombre_producto = request.form['nombre_producto']
    valor = request.form['valor']
    cantidad = request.form['cantidad']
    if nombre_producto and valor and cantidad:
        print("1")
        sql = """
        INSERT INTO public.producto(nombre_producto,Valor_Producto,Cantidad)VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (nombre_producto, valor, cantidad))
        con_bd.commit()
        flash("Registro Guardado", "info")
        return redirect(url_for('registar_datos'))
    else:
        flash("Registro No Guardado", "error")
        return redirect(url_for('registar_datos'))



@app.route('/editar_producto/<int:id_producto>', methods=['POST'])
def editar_producto(id_producto):
    cursor = con_bd.cursor()
    nombre_producto = request.form['nombre_producto']
    valor = request.form['valor']
    cantidad = request.form['cantidad']
    if nombre_producto and valor and cantidad:
        sql = """UPDATE producto SET  Nombre_Producto=%s, Valor_Producto=%s, Cantidad=%s WHERE id =%s"""
        cursor.execute(sql, (nombre_producto, valor, cantidad, id_producto))
        con_bd.commit()
        print('actualizar')
        return redirect(url_for('registar_datos'))
    else:
        print('error de actualizacion')
        return 'ERROR'

@app.route('/eliminar_producto/<int:id_producto>')
def eliminar_producto(id_producto):
    cursor = con_bd.cursor()
    sql = "DELETE FROM producto WHERE id = {0}".format(id_producto)
    cursor.execute(sql)
    con_bd.commit()
    return redirect(url_for('registar_datos'))


def crearTablaProducto():
    cursor = con_bd.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS producto(
        id serial NOT NULL,
        Nombre_Producto character varying(30),
        Valor_Producto character varying(30),
        Cantidad character varying,
        CONSTRAINT pk_producto_id PRIMARY KEY (id)
        );
    """)
    con_bd.commit()



def crearTablaUsuari():
    cursor = con_bd.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS usuari( 
                        id serial NOT NULL,
                        email character(50)  NOT NULL,
                        password character(50)  NOT NULL,
                        CONSTRAINT pk_usuari_id PRIMARY KEY (id)
                        );
                """)
    con_bd.commit()

if __name__=='__main__':
    crearTablaProducto()
    crearTablaUsuari()
    app.run(debug=True)