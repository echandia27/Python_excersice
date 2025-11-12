# 22. Gimnasio “StrongFit” – Cálculo de energía
# Como entrenador, quiero una función calcularEnergia() que reciba un número de repeticiones y devuelva un mensaje:

#     Si las repeticiones son menores de 5 → “Necesitas más esfuerzo”.
#     Si son 5 o más → “¡Buen trabajo!”.

def calcularEnergia(repeticiones):
    if  repeticiones <= 5:
        return("Necesitas más esfuerzo")
    else:
        return("¡Buen trabajo!")
    
num=int(input("Ingrese repeticiones "))
mensaje= calcularEnergia(num)
print(mensaje)
