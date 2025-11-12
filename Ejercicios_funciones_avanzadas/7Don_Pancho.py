# 7. Panadería “Don Pancho” – Control de producción diaria
# Como panadero, quiero una función hornear_pan(lotes) que use un for para indicar qué lote se está horneando.
# Si el lote es divisible por 3, mostrar “Verificación de calidad”.
# Al final, mostrar “Producción terminada”.

def hornear_pan():
    lote=int(input("Ingrese cuantos loques va realizar "))
    for i in range(1, lote+1):
        if i % 3 ==0:
            print(f"se esta horneando el lote {i} Verificación de calidad")
        else:
            print(f"se esta horneando el lote {i}")

hornear_pan()