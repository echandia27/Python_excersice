# 14. Academia “DevLoop” – Calculadora de factoriales
# Como estudiante de programación, quiero una función calcular_factorial(numero) que use un bucle for para calcular el factorial del número.
# Si el número ingresado es negativo, mostrar “Número inválido”.
# De lo contrario, mostrar el resultado.

def calcular_factorial(numero):
    if numero <= 0:
            return "Númeor invalido"
    
    resultado=1
    for i in range(1, numero+1 ):
        resultado *= i
    return resultado
    
numero=int(input("Ingrese número a calcular "))
print(f"El factorial del número {numero} es {calcular_factorial(numero)}")
