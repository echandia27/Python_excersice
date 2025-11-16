# 3) Tienda “Combo Pack” — Extender inventario
# Como supervisor, quiero una función extender_inventario(actual, nuevos) que valide que nuevos no esté vacío y una ambas listas.

# Muestra el tamaño total al final.
# Recorre la lista para destacar los recién agregados.
# Sugerencia: usa list.extend().

nuevo = [4,5,6,7]
viejo=[1,2,3,4]

def extender_inventario():
    if not nuevo:
        print("la lista esta vacia\n")
    
    punto_inicio= len(viejo)
    viejo.extend(nuevo)

    print(f"la lista actualizada es: {len(viejo)}\n")


    for i, e in enumerate(viejo, start=1):
        if i > punto_inicio:
            print(f"{i}.{e} (NUEVO)")
        else:
            print(f"{i}.{e}")



extender_inventario()
