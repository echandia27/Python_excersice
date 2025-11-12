# 17. Panadería “Don Pancho” – Producción diaria
# Como panadero, quiero usar un for del 1 al 12.
# Si el número es 6, mostrar “Mitad de la producción completada”.
# Si es 12, mostrar “¡Día finalizado!”.

for i in range(1, 13):
    if i == 6:
        print("Mitad de la producción completada")
    elif i == 12:
        print("¡Día finalizado!")
    else:
        print(f"llevamos {i} panes")


