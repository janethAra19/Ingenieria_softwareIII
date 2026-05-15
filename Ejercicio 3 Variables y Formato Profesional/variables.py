# Parte A

producto = "Pan Integral"  
costo    = 12.50            
cantidad = 20               

total = costo * cantidad

print(f"Reporte: El producto {producto} tiene un valor total de ${total:.2f}")


# Parte B
monto_credito = 50000
tasa_mensual  = 0.015
plazo_meses   = 12

interes_total = monto_credito * tasa_mensual * plazo_meses

print("--- RESUMEN DE CRÉDITO ---")
print(f"Monto base: ${monto_credito}")
print(f"Intereses generados a {plazo_meses} meses: ${interes_total}")