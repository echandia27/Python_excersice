# 4. Banco “PythonBank” – Evaluador de crédito
# Como asesor financiero, quiero una función evaluar_credito(ingresos, edad) que:

#     Apruebe el crédito si los ingresos son mayores de 2 millones y la edad está entre 25 y 60.
#     Si no cumple, mostrar “Crédito rechazado”.
#     Usar condicionales dentro de la función.

def evaluar_credito():
    ingresos=int(input("Ingrese sus ingresos "))
    edad=int(input("Ingrese edad "))
    if ingresos > 2000000 and edad >= 25 and edad <=60:
        print("Credito Aprobado")
    else:
        print("Credito Rechazado")

evaluar_credito()
