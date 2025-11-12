# 25. Restaurante “BuenaFunción” – Verificación de turno
# Como gerente, quiero una función verificarTurno(hora) que determine:

# Si la hora es menor que 12 → “Turno de mañana”.
# Si está entre 12 y 18 → “Turno de tarde”.
# Si es mayor → “Turno de noche”.
# El programa principal debe pedir la hora e imprimir el resultado.

def verificarTurno(hora):
    if hora <= 12:
        return "Turno de mañana"
    elif hora > 12 and hora < 18:
        return "Turno de tarde"
    else:
        return "Turno de noche"

ingreso=int(input("ingrese hora de entrada "))
print(verificarTurno(ingreso) )