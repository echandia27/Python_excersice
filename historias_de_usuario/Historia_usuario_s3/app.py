import servicios
import archivos
inventario=[]

# Aqui esta el menu de la aplicacion que se repetira hasta introducir un 9 que lo sacaria del bucle
while True:

    print("\n<--Que accion desea realizar -->")
    print("1 Agregar producto")
    print("2 Mostrar inventario")
    print("3. Buscar Producto")
    print("4. Actualizar Producto")
    print("5. Eliminar Producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir\n")

    try:
        opcion=int(input("Ingrese el número a la cual quiere ir: "))
        if opcion < 1 or opcion > 9:
            opcion=int(input("Ingrese un número valido al cual quiere ir: "))
    except ValueError:
        print("\nIngrese un parametro valido")
        
#Aqui estan los codigos para ir a la variable que deseas ejecutar
    if opcion == 1:
        servicios.agregar(inventario)
    elif opcion == 2:
        servicios.mostrar(inventario)
    elif opcion == 3: 
        servicios.buscar(inventario)
    elif opcion == 4:
        servicios.actualizar(inventario)
    elif opcion == 5:
        servicios.Eliminar_producto(inventario)
    elif opcion == 6:
        servicios.calcular(inventario)
    elif opcion ==7:
        archivos.guardar(inventario)
    elif opcion ==8:
        inventario = archivos.cargar("inventario.csv")

    elif opcion ==9:
        print("\nSaliendo del programa Suerte!")
        break 

        
    else:
        print("\nIngrese un numero correcto")
