# 7) Deportes “Marcador frecuente” — Contar apariciones
# Como estadístico, quiero una función contar_marcador(marcadores, valor) que valide tipos y devuelva cuántas veces aparece valor.

# Si no aparece, retornar 0.
# Recorre la lista para imprimir posiciones donde aparece.
# Sugerencia: usa list.count().

marcadores=["1","2","3","3","4","3","5","3"]

def contar_marcadores(marcadores, valor):
    
    total=marcadores.count(valor)
    if total == 0:
        return 0
    
    for i in range(len(marcadores)):
        if marcadores[i]== valor:
            print(f"aparece en posicion {i}")
    return total

valor=input("Ingrese marcador ")

resultado=contar_marcadores(marcadores, valor)
print(f"total apariciones {resultado}")

        