# 8. Cine “MovieLoop” – Calculadora de entradas
# Como cajero, quiero una función calcular_entradas() que pida edades de los clientes hasta que se ingrese 0.
# Aplicar precio:

#     Menores de 12 → $5.000
#     De 12 a 59 → $8.000
#     Mayores de 60 → $4.000
#     Usar un while y condiciones.

def calcular_entrada():
    while True:
        edad=int(input("ingrese su edad "))
        if edad == 0:
            break
        elif edad <= 11:
            print("El precio es de $5.000")
        elif edad >= 12 and edad < 59:
            print("El precio es de $8.000")
        else:
            print("El precio es de $4.000")

calcular_entrada()