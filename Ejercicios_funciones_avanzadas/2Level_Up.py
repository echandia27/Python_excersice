# 2. Gimnasio “Level Up” – Control de repeticiones
# Como entrenador, quiero una función repeticiones(n) que use un bucle for para mostrar las repeticiones del 1 al número indicado.
# Si el número actual es par, mostrar “Excelente forma”, si no, “Mantén el ritmo”.

def repeticiones(n):
    for i in range(1, n+1):
        if i % 2 ==0:
            print(f" {i} Excelente forma")
        else:
            print(f" {i} Mantén el ritmo")
        
numero=int(input("Ingresa numero de repeticiones "))
repeticiones(numero)

