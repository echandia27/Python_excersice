from usuarios import iniciar_sesion
import equipos
import prestamos
import reportes

def menu_principal():
    while True:
        print("\n<=====MENU PRINCIPAL======>")
        print("1. Gestion de Equipos")
        print("2. Gestion de Prestamos")
        print("3. Consultar Historial")
        print("4. Salir\n")

        try:
            opcion=int(input("Ingrese el numero de donde quiere ir"))
            if opcion <= 0 or opcion >= 6:
                print("Ingrese un numero entre los parametros")

            elif opcion == 1:
                menu_gestion_equipos()
            
            elif opcion == 2:
                menu_gestion_prestamos()

            elif opcion == 3:
                menu_reportes()

            elif opcion ==4:
                print("Hata la vista!")
                break

            else:
                print("\nopcion no valida intente nuevamente\n")
               
        except ValueError:
            print("Ingrese un numero entero")

        #submenu de equipos
def menu_gestion_equipos():
    while True:
        print("\n-----GESTION EQUIPOS-----")
        print("1. Registrar nuevo equipo")
        print("2. Mostrar equipos")
        print("3. Consultar equipo por ID")
        print("4. volver\n")

        try:
            opcion=int(input("Ingrese el numero de donde quiere ir"))
            if opcion <= 0 or opcion >= 5:
                print("Ingrese un numero entre los parametros")

            elif opcion == 1:
                equipos.registrar_equipo()
            elif opcion ==2:
                equipos.listar_equipos()
            elif opcion == 3:
                equipos.consultar_equipo()
            elif opcion ==4:
                print("Volviste al menu anteior")
                break
            
            
            else:
                print("\nOpcion invalida intente nuevamente\n")
               
        except ValueError:
            print("Ingrese un numero entero")


#submenu de equipos-------------------------------------------

def menu_gestion_prestamos():
    while True:
        print("\n-----GESTION PRESTAMOS-----")
        print("1. Registrar solicitud de prestamo")
        print("2. Aprobar/Rechazar solicitudes")
        print("3. Registrar devolucion")
        print("4. volver\n")

        try:
            opcion=int(input("Ingrese el numero de donde quiere ir"))
            if opcion <= 0 or opcion >= 5:
                print("Ingrese un numero entre los parametros")

            elif opcion == 1:
                prestamos.registrar_prestamo
            elif opcion ==2:
                prestamos.aprobar_prestamo
            elif opcion == 3:
                prestamos.registar_devolucion
            elif opcion ==4:
                print("Volviste al menu anteior")
                break
            
            else:
                print("\nOpcion invalida intente nuevamente\n")
                
        except ValueError:
            print("Ingrese un numero entero")

#menu reportes

def menu_reportes():
    while True:
        print("\n--- REPORTES ---")
        print("1. Mostrar equipos disponibles")
        print("2. Mostrar equipos prestados")
        print("3. Mostrar equipos por categoría")
        print("4. Mostrar historial de préstamos")
        print("5. Volver al menú principal")

        try:
            opcion=int(input("Ingrese el numero de donde quiere ir"))
            if opcion <= 0 or opcion >= 5:
                print("Ingrese un numero entre los parametros")

            elif opcion == 1:
                reportes.reporte_equipos_disponibles()
            elif opcion ==2:
                reportes.reporte_equipos_prestados()
            elif opcion == 3:
                reportes.reporte_por_categoria()

            elif opcion ==4:
                reportes.reporte_historial_prestamos()

            elif opcion ==5:
                print("Volviste al menu anteior")
                break
            
            else:
                print("\nOpcion invalida intente nuevamente\n")
                
        except ValueError:
                print("Ingrese un numero entero")
     
    



#ejecucion del programa



if __name__=="__main__":
     if iniciar_sesion():
          menu_principal()
     




