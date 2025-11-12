# 12. Gimnasio “Level Up” – Control de repeticiones
# Como deportista, quiero ingresar un número de repeticiones y usar un for para imprimir “Repetición X completada”.
# Si X es divisible por 3, mostrar además “¡Excelente ritmo!”.
repeticion=int(input("Ingrese numero de repeticiones"))
for i in range(1, repeticion+1):
    if i % 3 == 0:
        print("¡Excelente ritmo!")
    else:
        print(f"Repeticion {i} completada")