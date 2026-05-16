precio_venta = 850
precio_costo = 520
costo_actual = 12000
usuarios_anteriores = 80
usuarios_nuevos = 124 



ganancia = precio_venta - precio_costo
margen = ganancia / precio_venta * 100
ahorro = costo_actual * 0.08
crecimiento = ((usuarios_nuevos - usuarios_anteriores) / usuarios_anteriores * 100)

print("La ganancia es de" ,  ganancia)
print(f"La ganancia es de {ganancia}")
print(f"El margen de ganancia es {margen}")
print(f"Ahorro mensual:  {ahorro}")
print(f"Crecimieto de usuarios {crecimiento}")