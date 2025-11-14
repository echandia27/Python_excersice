# 1) Restaurante “Menú Dinámico” — Agregar plato del día
# Como chef, quiero una función agregar_plato(menu, plato) que valide que plato no esté vacío y lo agregue a la lista menu.

#     Si el plato ya existe, mostrar “plato duplicado”.
#     Recorre el menú al final para imprimirlo numerado.
#     Sugerencia: usa list.append().

Menu_dia=[]

def agregar_plato():
    plato=str(input("Agregue un plato nuevo al menu\n"))
    Menu_dia.append({"plato": plato,})

    for plat in Menu_dia:
        if plat["plato"].lower() == plato.lower():
            print("plato Agregado")
        elif plat in Menu_dia:
            print("plato duplicado")


def mostrar():
    print("<==EL MENU DE HOY ES==>")
    for plat in Menu_dia:
        print(f"- {plat["plato"]}\n")

    if Menu_dia == []:
        print("EL menu esta vacio")
    elif plat in Menu_dia:
        print("plato duplicado")



while True:
    print("\n<==== MENU DEL DIA ====>")
    print("1. Mostrar menu")
    print("2. Agregar plato")
    print("3. Salir")

    try:
        
        opcion=int(input("Ingrese el numero de lo que desea hacer\n"))
    except ValueError:
        print("Ingrese un valor valido")
        continue

    if opcion == 1:
        mostrar()

    elif opcion == 2:
        agregar_plato()

    elif opcion == 3:
        print("Sesion Terminada\n")
        break
    else:
        print("ingrese un valor correcto")
