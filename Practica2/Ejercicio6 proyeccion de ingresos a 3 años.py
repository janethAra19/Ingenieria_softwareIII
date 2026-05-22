precio      = 149.0
usuarios_anio1 = 200

usuarios_anio2 = usuarios_anio1 * 1.5   # 150% de crecimiento

usuarios_anio3 = usuarios_anio2 * 1.5

ingreso_anio1 = usuarios_anio1 * precio * 12

ingreso_anio2 = usuarios_anio2 * precio * 12

ingreso_anio3 = usuarios_anio3 * precio * 12

ingreso_total = ingreso_anio1 + ingreso_anio2 + ingreso_anio3

print('====== PROYECCIÓN DE INGRESOS ======')
print()
print(f'Precio mensual por usuario: ${precio}')
print()
print('------------------------------------')
print()
print(f'Año 1 | {int(usuarios_anio1)} usuarios | ${ingreso_anio1:,.2f}')
print()
print(f'Año 2 | {int(usuarios_anio2)} usuarios | ${ingreso_anio2:,.2f}')
print()
print(f'Año 3 | {int(usuarios_anio3)} usuarios | ${ingreso_anio3:,.2f}')
print()
print('------------------------------------')
print()
print(f'Ingreso acumulado 3 años : ${ingreso_total:,.2f}')
print()
print('====================================')