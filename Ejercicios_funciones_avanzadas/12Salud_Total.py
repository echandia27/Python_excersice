# 12. Hospital “Salud Total” – Evaluador de signos vitales
# Como médico, quiero una función evaluar_paciente() que reciba frecuencia cardiaca y temperatura corporal.
# Si ambos valores están fuera del rango normal (FC > 100 o Temp > 38), mostrar “Paciente en observación”.
# Repetir el proceso con varios pacientes en un bucle while.

def evaluar_paciente():
    total=1
    while total != 5:
        cardio=int(input("Ingrese frecuencia cardiaca "))
        temperatura=int(input("Ingrese temperatura corporal"))
        if cardio < 100 and temperatura > 38:
            print(f"paciente {total} en observación")
        else:
            print(f"paciente {total} casi bien")
        total+=1

evaluar_paciente()