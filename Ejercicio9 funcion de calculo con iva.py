def calcular_con_iva(precio, tasa_iva=0.16):
    total = precio * (1 + tasa_iva)
    return total

precio_mensual = 149.0
precio_anual   = precio_mensual * 12  # 1788.0

print('=== PRECIOS CON IVA ===')
print()
print(f'Plan mensual (IVA 16%) : ${calcular_con_iva(precio_mensual):.2f}')
print()
print(f'Plan anual   (IVA 16%) : ${calcular_con_iva(precio_anual):.2f}')
print()
print(f'Plan mensual (IVA 8%)  : ${calcular_con_iva(precio_mensual, 0.08):.2f}')
print()
print('======================')