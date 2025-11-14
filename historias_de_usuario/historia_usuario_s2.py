# 1. Validación de datos con condicionales:

#     Crea un menú que pregunte al usuario qué acción desea realizar:
#         Agregar producto
#         Mostrar inventario
#         Calcular estadísticas
#         Salir
#     Usa condicionales if, elif y else para procesar la opción elegida.
#     Si el usuario ingresa una opción inválida, muestra un mensaje de error y pide nuevamente la entrada.

# 2. Implementar un bucle para múltiples registros:

#     Envuelve el menú en un bucle while que continúe ejecutándose hasta que el usuario elija salir.
#     Permite agregar varios productos seguidos (nombre, precio y cantidad).
#     Cada producto debe almacenarse como un diccionario dentro de una lista llamada inventario.
#         producto = {"nombre": "Lápiz", "precio": 500, "cantidad": 3}
#         inventario.append(producto)

# 3. Mostrar todos los productos del inventario:

#     Implementa una opción en el menú que recorra el inventario con un bucle for.
#     Muestra todos los productos en un formato claro:
#         Producto: Lápiz | Precio: 500 | Cantidad: 3
#     Si el inventario está vacío, muestra un mensaje que lo indique.

# 4. Calcular estadísticas básicas:

#     Implementa en el menú una opción para calcular:
#         El valor total del inventario (sumatoria de precio × cantidad).
#         La cantidad total de productos registrados.
#     Muestra los resultados usando print() de manera clara.

# 5. Documentación y limpieza del código:

#     Comenta el código explicando la funcionalidad de cada sección (menú, bucle, validación, estadísticas).
#     Estructura el código en funciones simples:
#         agregar_producto()
#         mostrar_inventario()
#         calcular_estadisticas()
#     Deja un comentario final resumiendo el objetivo de la semana.

#Aqui creamos un inventario vacio que se ira llenando a medida que agreguemos productos
inventario=[]

#Aqui agregamos una variable para que siempre que se llame se introduzca un producto          
def agregar(inventario):
    
    nombre=str(input("Ingresa el nombre "))
    precio=int(input("Ingresa el precio "))
    if precio <= 0:
        print("Valor invalido")
        precio=int(input("Ingresa el precio "))
    cantidad=int(input("Ingresa la cantidad "))
    if cantidad <= 0:
        print("Valor invalido")
        cantidad=int(input("Ingresa la cantidad "))
    producto={"nombre" : nombre, "precio" : precio, "cantidad" : cantidad }
    inventario.append(producto)

#Aqui agregamos una variable para que siempre que se llame busque los productos en la aplicacion
def mostrar(inventario):

    for producto in inventario:
        print(f"producto:{producto["nombre"]} precio:{producto["precio"]} cantidad:{producto["cantidad"]}")
          
    else:
        print("<-----El inventario esta vacio------>")

#Aqui agregamos una variable para que siempre que se llame haga los calculos del inventario
def calcular(inventario):
    print("<----- Calculos del Inventario ----->")
    valor_total=0
    for producto in inventario:
        valor_total+= producto["precio"]* producto["cantidad"]
    total_producto= len(inventario)

    print(f"el valor total del inventario es: {valor_total}")
    print(f"el cantidad total de productos registrados es: {total_producto}")

# Aqui esta el menu de la aplicacion que se repetira hasta introducir un 4
while True:

    print("<--Que accion desea realizar -->")
    print("1 Agregar producto")
    print("2 Mostrar inventario")
    print("3 Calcular estadísticas")
    print("4 Salir")

    opcion=int(input("Ingrese el número a la cual quiere ir "))
    if opcion < 1 or opcion > 4:
        opcion=int(input("Ingrese un número valido al cual quiere ir: "))
        
#Aqui estan los codigos para ir a la variable que deseas ejecutar
    elif opcion == 1:
        agregar(inventario)
    elif opcion == 2:
        mostrar(inventario)
    elif opcion == 3: 
        calcular(inventario)
        
    else:
        print("Saliendo del programa Suerte!")
        break 



