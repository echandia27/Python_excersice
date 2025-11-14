# 15. Empresa “TechManager” – Simulador de rendimiento laboral
# Como jefe de equipo, quiero una función evaluar_empleado(nombre, horas) que:

#     Use un bucle for para simular las horas trabajadas (de 1 hasta horas).
#     Si la hora es mayor de 8, contar como hora extra.
#     Al final, calcular el total de horas normales y extras.
#     Mostrar un resumen del empleado.

def evaluar_empleado(nombre,hora):
    extra=0
    for i in range(1, hora+1):
        if i > 8:
            extra+= 1
        print(f"{nombre} a trabajado {i} horas")
        
    horas_normal=hora-extra   
    print("Resumen del empleado")
    print(f"empleado {nombre}")
    print(f"ha trabado {horas_normal}")
    print(f" y {extra} horas extra")

    

nombre= str(input("Ingrese nombre "))
hora=int(input("Ingrese horas trabajadas "))
evaluar_empleado(nombre, hora)