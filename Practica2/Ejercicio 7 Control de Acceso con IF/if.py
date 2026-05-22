print('--- Prueba 1: status_usuario = "free" ---')
status_usuario = "free"

if status_usuario == "premium":
    print("Acceso Total")
else:
    print("Acceso Limitado")

print()

print('--- Prueba 2: status_usuario = "premium" ---')
status_usuario = "premium"

if status_usuario == "premium":
    print("Acceso Total")
elif status_usuario == "admin":
    print("Acceso Administrador")
else:
    print("Acceso Limitado")