# 5. Escuela “Aprende Más” – Promedio de notas
# Como profesor, quiero una función promedio_notas() que reciba tres notas y calcule el promedio.
# Si el promedio es mayor o igual a 3.0 → mostrar “Aprobado”, de lo contrario “Reprobado”.
# Debe repetirse para varios estudiantes usando un while.

def promedio_notas():
    estudiante=1
    while estudiante !=5 :
        nota1=float(input("INgrese su primera nota "))
        nota2=float(input("inregese su segunda nota "))
        nota3=float(input("ingrese su tercera nota "))
        notafinal= (nota1 + nota2 + nota3) /3
        
        estudiante +=1

        if notafinal >= 3:
            print("Aprobado")
        else:
            print("Reprobado")


promedio_notas()    