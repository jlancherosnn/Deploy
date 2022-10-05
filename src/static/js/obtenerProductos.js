function obtenerProductos(id){
    document.getElementById('formulario').action = '/editar_producto/'+id
    document.getElementById('boton_form').innerHTML = 'Actualizar'
    nombreactual = document.getElementById('tabla_nombre'+id).innerHTML
    valoroactual = document.getElementById('tabla_valor'+id).innerHTML
    cantidadactual = document.getElementById('taba_cantidad'+id).innerHTML

    document.getElementById('nombre_producto').value = nombreactual
    document.getElementById('valor').value = valoroactual
    document.getElementById('cantidad').value = cantidadactual

}