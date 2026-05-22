nombre_producto = 'EduTrack Pro'

precio_unitario = 149.0

unidades_disponibles = 30

categoria = 'Software educativo'

valor_inventario = precio_unitario * unidades_disponibles

print('=== REPORTE DE PRODUCTO ===')
print()
print(f'Producto  : {nombre_producto}')
print()
print(f'Categoría : {categoria}')
print()
print(f'Precio    : ${precio_unitario:.2f}')
print()
print(f'Unidades  : {unidades_disponibles}')
print()
print(f'Valor total inventario: ${valor_inventario:.2f}')
print()
precio_mensual = 149.0
print()
descuento_anual = 0.20
print()
meses = 12
print()
total_anual = precio_mensual * meses * (1 - descuento_anual)

print('=== PLAN ANUAL ===')
print()
print(f'Precio mensual : ${precio_mensual:.2f}')
print()
print(f'Descuento anual: 20%')
print()
print(f'Total a pagar  : ${total_anual:.2f}')