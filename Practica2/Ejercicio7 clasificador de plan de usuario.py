planes = ['gratuito', 'basico', 'profesional', 'empresarial']

for plan_usuario in planes:
    print(f"\n--- plan_usuario = '{plan_usuario}' ---")
    print()
    if plan_usuario == 'gratuito':
        print()
        print("Acceso Limitado — 3 proyectos máximo")
        print()
    elif plan_usuario == 'basico':
        print()
        print("Acceso Estándar — 10 proyectos")
        print()
    elif plan_usuario == 'profesional':
        print()
        print("Acceso Completo — proyectos ilimitados")
        print()
    else:
        print()
        print("Acceso Total + Soporte prioritario")