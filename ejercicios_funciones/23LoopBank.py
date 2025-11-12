# 23. Banco “LoopBank” – Simulación de intereses
# Como analista financiero, quiero una función calcularInteres() que reciba un monto y una tasa (porcentaje) y retorne el valor final después de aplicar el interés una vez.
# El programa principal debe pedir los datos y mostrar el resultado.

def calcular_intereses(monto, tasa):
    interes = monto * (tasa/100)
    total = monto + interes
    return total
    
# programa principal
monto=float(input("Ingrese el monto"))
tasa=float(input("ingrese interes"))

valor_final= calcular_intereses(monto, tasa)
print(f"su valor final es {valor_final} ")