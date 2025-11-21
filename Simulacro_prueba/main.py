from usuarios import iniciar_sesion
from equipos import listar_equipos, registrar_equipos, actualizar_equipo
from prestamos import registrar_prestamo, devolver_prestamo
from reportes import generar_reporte

def menu():
    while True:
        print("\n<=====MENU PRINCIPAL======>")
        print("1. Gestion de Equipos")
        print("2. Gestion de Prestamos")
        print("3. Conultar Historial")
        print("4. Exportar Reporte CSV")
        print("5. Salir\n")

        try:
            opcion=int(input("Ingrese el numero de donde quiere ir"))
            if opcion <= 0 or opcion >= 5:
                print("Ingrese un numero entre los parametros")
            else:
                return opcion
            
        except ValueError:
                print("Ingrese un numero entero")

if __name__=="__main__":
     if iniciar_sesion():
          menu()
     




