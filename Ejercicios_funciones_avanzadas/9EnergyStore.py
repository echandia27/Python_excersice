# 9. Tienda “EnergyStore” – Simulador de puntos
# Como cliente, quiero una función calcular_puntos(compras) que use un for para recorrer la cantidad de compras (ingresada por el usuario).
# Si el número de compra es múltiplo de 3, agregar 10 puntos; en caso contrario, agregar 5.
# Al final, mostrar los puntos totales.

def calcular_puntos():
    puntos_totales=0
    compras=int(input("Ingrese numero de compras "))
    for i in range(1, compras+1):
        if i % 3 == 0:
            print(f" {i} agregue 10 puntos")
            puntos_totales+=10
        else:
            print(f" {i} agregue 5 puntos")
            puntos_totales+=5
    return puntos_totales

puntos_finales= calcular_puntos()
print(f"calcular {puntos_finales} ")