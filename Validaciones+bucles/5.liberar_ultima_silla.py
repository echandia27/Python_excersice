# 5) Cine “Liberar última silla” — Quitar el final
# Como administrador de sala, quiero una función liberar_ultima(butacas) que valide que hay elementos y quite el último asiento reservado; debe retornar el valor removido.

# Si no hay butacas, mostrar “sala vacía”.
# Imprimir el estado final.
# Sugerencia: usa list.pop() sin índice.

butacas=["a1","a2","a3"]

def liberar_ultima():
    if len(butacas) == 0:
        print("Lista vacia")
        return None
    ultima=butacas.pop()
    print(f"butaca liberada {ultima}")

    print("Nuevo estado de las reservas")

    for i in butacas:
        print(f"- {i}")
    return ultima

liberar_ultima()

