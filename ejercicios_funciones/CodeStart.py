# 15. Academia “CodeStart” – Contador de ejercicios completados
# Como estudiante, quiero usar un for del 1 al número que indique.
# Si el número es múltiplo de 5, mostrar “¡Gran avance!”.
# Si no, solo mostrar “Ejercicio X completado”.

numero=int(input("Ingrese cuantos ejercicios lleva "))
for i in range(1, numero+1):
    if i % 5 == 0:
        print("!Gran Avance¡")
    else:
        print(f"Ejercicio {i} completado")
