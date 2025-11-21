from usuarios import login
from equipos import listar_equipos, registrar_equipos, actualizar_equipo
from prestamos import registrar_prestamo, devolver_prestamo
from reportes import generar_reporte

def menu():
    
    print("\n<=====MENU PRINCIPAL======>")
    print("1. Gestion de equipos")
    print("2. Gestion de prestamos")
    print("3. Reportes")
    print("4. Salir\n")

    try:
        opcion=int(input("Ingrese el numero de donde quiere ir"))
        if opcion <= 0 or opcion >= 5:
            print("Ingrese un numero entre los parametros")
        else:
            return opcion
    except ValueError:
            print("Ingrese un numero entero")




