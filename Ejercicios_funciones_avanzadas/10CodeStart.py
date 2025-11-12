# 10. Academia “CodeStart” – Tabla de multiplicar personalizada
# Como estudiante, quiero una función tabla_multiplicar(numero) que use un for para mostrar la tabla del número dado hasta el 10.
# Si el resultado es mayor de 50, mostrar también “Resultado alto”.

def tabla_multiplicar():
    numero=int(input("Ingrese un munero "))
    for i in range(1, 11):
        resultado = numero * i
        print(f" {numero} x {i} = {resultado}")

        if resultado > 50:
            print("resultado alto")

tabla_multiplicar()

        