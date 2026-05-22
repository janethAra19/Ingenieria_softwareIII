def aplicar_descuento(precio):
    nuevo_precio = precio * 0.9
    return nuevo_precio


precio_producto = 149

precio_final = aplicar_descuento(precio_producto)

print("Precio con descuento de lanzamiento:", precio_final)