#Aqui creamos un inventario vacio que se ira llenando a medida que agreguemos productos


#Aqui agregamos una variable para que siempre que se llame se introduzca un producto          
def agregar(inventario):
    try:
        nombre=str(input("Ingresa el nombre: "))
        #verifica si el producto ya existe 
        for producto in inventario:
            if producto["nombre"].lower()== nombre.lower():#.lower es para que sea minisculas
                print("Producto ya existe, se sumara cantidad\n")

                while True:
                    try:
                        cantidad= int(input("Ingrese cantidad a agregar"))
                        if cantidad <=0:
                            print("valor invalido, debe ser mayor a 0")
                            continue
                        break
                    except ValueError:
                        print("ingrese un numero entero valido")
                producto["cantidad"]+= cantidad
                print("Se sumo la cantidad\n")
                return
        # como el producto no existe se crea 
        while True:
            try:
                cantidad=int(input("Ingrese la cantindad: "))
                if cantidad <=0:
                    print("Valor invalido\n")
                    continue
                break
            except ValueError:
                print("Ingrese un número entero valido")
                
        while True:
            try:
                precio=float(input("Ingrese el precio del producto: "))
                if precio <= 0:
                    print("ingrese un valor positivo")
                    continue
                break
            except ValueError:
                print("ingrese un numero valido")
        
        nuevo_producto= {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }

        inventario.append(nuevo_producto)
        print("\nEl producto fue agregado correctamente\n")

    except Exception as e:
        print(f"Error Inesperado {e}\n") #se empieza con un try y lo que hace es que no salga un error
                                        #indesperado en la funcion
       

#Avariable mostrar para mostrar todo el inventario
def mostrar(inventario):
        if not inventario:
            print("\n<------El inventario esta vacio------->\n")
            return
        for producto in inventario:
            print(f"producto:{producto['nombre']} cantidad:{producto['cantidad']} precio:{producto['precio']}\n")

def buscar(inventario):
    buscando=str(input("Ingrese el nombre del producto a buscar: "))
    for producto in inventario:
        if buscando == producto["nombre"]:
            print(f"El producuto: nombre {producto['nombre']}, cantidad {producto['cantidad']}, cantidad {producto['precio']} ")

def actualizar(inventario):
    if not inventario:
        print("\nInventario vacio")
        return
    try:
        actualizar_inventario=str(input("Ingrese el nombre del producto a actualizar: "))
    except ValueError:
        print ("digite un nombre de producto")

    for producto in inventario:
        if producto["nombre"] == actualizar_inventario:
            print("\nProducto encontrado")
            print(producto)

            print("\n Que desea actualizar")
            print("1. Cantidad")
            print("2. Precio")
            print("3. para cambiar las 2\n")

            try:
                opcion=int(input("Ingrese la opcion a elegir: "))

                if opcion == 1:
                    producto["cantidad"]= int(input("Nueva Cantidad: "))
                elif opcion == 2:
                    producto["precio"]= int(input("Ingrese nuevo precio: "))
                elif opcion ==3:
                    producto["cantidad"]= int(input("Nueva Cantidad: "))
                    producto["precio"]= int(input("Ingrese nuevo precio: "))
                else:
                    print("Opcion no valida\n")
            except ValueError:
                print("Ingrese un parametro correcto")
    print(f"\n{producto}\n")
    
def Eliminar_producto(inventario):
    try:
        eliminar=str(input("Ingrese el nombre del producto que desea eliminar\n"))
    except ValueError:
        print("digite un parametro valido")
        return
    for producto in inventario:
        if producto["nombre"]== eliminar:
            inventario.remove(producto)
            print("\nProducto Eliminado con exito\n")
            return

    print("\nProducto no encontrado\n")


# Aqui agregamos una variable para que siempre que se llame haga los calculos del inventario
def calcular(inventario):
    if not inventario:
        print("El inventario esta vacio")
        return None
    #se ponen las estadisticas antes de crear el menu y se llaman mas adelante, ademas se unifican 
    #en estadisticas para poder tirar return al final
    unidades_totales= sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    estadisticas = (unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock)
    
    
    while True:
        try:
            print("\n<----- Calculos del Inventario ----->\n")
            print("1. Cantidad Total Inventario:")
            print("2. Valor total")
            print("3. Producto mas Caro")
            print("4. Producto con mayor Stock")
            print("5. Menu anterior")

            try:
                opcion2=int(input("Ingrese el número de la opcion que desea realizar"))
                if opcion2 <= 0 or opcion2 >= 6:
                    print("Ingrese un número correcto")
                elif opcion2 == 1:
                    print(f"\nLas Unidades totales son: {unidades_totales}\n")
                  
                elif opcion2 == 2:
                    print(f"\nEl valor total del inventario es: {valor_total}\n ")
                elif opcion2 == 3:
                    print(f"El producto mas caro: {producto_mas_caro['nombre']} (Precio: {producto_mas_caro['precio']})\n")

                elif opcion2 == 4:
                    print(f"Producto con mayor stock: {producto_mayor_stock['nombre']} (Cantidad: {producto_mayor_stock['cantidad']}\n)")
                    
                elif opcion2 == 5:
                    print("usted a vuelto al menu anterior")
                    break

            except ValueError:
                print("Ingrese un parametro valido")
                continue
        
        except Exception as e:
            print(f"Error Inesperado {e}\n") 
    return estadisticas       
                    

   