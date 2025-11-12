# 24. Escuela “Aprende con Funciones” – Promedio de notas
# Como profesor, quiero crear una función promedioNotas() que reciba tres notas y calcule el promedio.
# Si el promedio es mayor o igual a 3.0, mostrar “Aprobado”; si no, “Reprobado”.

def promedionotas():
    notafinal= (nota1 + nota2 + nota3) / 3
    return notafinal

nota1= float(input("ingrese la primera nota "))
nota2= float(input("Ingrese la segunda nota "))
nota3= float(input("Ingrese la tercera nota "))

if promedionotas() >= 3:
    print(f"Aprobado {promedionotas()} ")
else:
    print(f"Reprobado {promedionotas()} ")
