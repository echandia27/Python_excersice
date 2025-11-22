from usuarios import iniciar_sesion
import equipos
import prestamos
import reportes

def menu_principal():
    while True:
        print("\n<=====MENU PRINCIPAL======>")
        print("1. Gestion de Equipos")
        print("2. Gestion de Prestamos")
        print("3. Conultar Historial")
        print("4. Exportar Reporte CSV")
        print("5. Salir\n")

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
        print("2. Listar nuevo equipo")
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
                prestamos.solicitar_prestamo()
            elif opcion ==2:
                prestamos.aprobar_rechazar_prestamo()
            elif opcion == 3:
                prestamos.registrar_devolucion()
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
        print("\n-----REPORTES-----")
        print("1. Consultar historial por Equipo")
        print("2. Consultar historial por Usuario")
        print("3. Exportar reporte CSV por mes y año")
        print("4. volver\n")

        try:
            opcion=int(input("Ingrese el numero de donde quiere ir"))
            if opcion <= 0 or opcion >= 5:
                print("Ingrese un numero entre los parametros")

            elif opcion == 1:
                reportes.historial_por_equipo()
            elif opcion ==2:
                reportes.historial_por_usuario()
            elif opcion == 3:
                reportes.exportar_reporte()
            elif opcion ==4:
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
     




