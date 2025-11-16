# 2) Teatro “Butacas VIP” — Insertar reserva en posición**  
# *Como encargado de reservas,* quiero una función `insertar_reserva(butacas, nombre, posicion)`
#  que **valide** que `posicion` esté en rango y **ubique** la reserva en esa posición.  
# - Si la posición no es válida, no inserta y muestra error.  
# - Luego, recorre la lista para confirmar el orden.  


# **Sugerencia:** usa `list.insert()`.

butacas=["juan","carlos", "perdo", "jaime"]


def reserva(butacas, nombre, posicion):
    if nombre in butacas :
        print("Ya existe")
    elif not posicion in range(len(butacas)):
        print("fuera de rango")   
    else:
        butacas.insert(posicion, nombre)
        for i, n in enumerate(butacas):
            i+=1
            print(f"{i}. {n}")

reserva(butacas, "alfredo", 2)
reserva(butacas, "perdo", 1)
