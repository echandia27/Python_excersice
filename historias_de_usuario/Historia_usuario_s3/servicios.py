#Aqui creamos un inventario vacio que se ira llenando a medida que agreguemos productos


#Aqui agregamos una variable para que siempre que se llame se introduzca un producto          
def agregar(inventario):
    try:
        nombre=str(input("Ingresa el nombre: "))
        precio=int(input("Ingresa el precio: "))
        if precio <= 0:
            print("Valor invalido")
            precio=int(input("Ingresa el precio: "))
        cantidad=int(input("Ingresa la cantidad: "))
        if cantidad <= 0:
            print("Valor invalido\n")
            cantidad=int(input("Ingresa la cantidad: "))
        producto={"nombre" : nombre, "precio" : precio, "cantidad" : cantidad }
        inventario.append(producto)
    except ValueError:
        print("Ingresa lo que se te pide")

#Aqui agregamos una variable para que siempre que se llame busque los productos en la aplicacion
def mostrar(inventario):
        if not inventario:
            print("\n<-----El inventario esta vacio------>\n")
            return
        for producto in inventario:
            print(f"producto:{producto["nombre"]} precio:{producto["precio"]} cantidad:{producto["cantidad"]}")

#Aqui agregamos una variable para que siempre que se llame haga los calculos del inventario
def calcular(inventario):
    print("\n<----- Calculos del Inventario ----->")
    valor_total=0
    for producto in inventario:
        valor_total+= producto["precio"]* producto["cantidad"]
    total_producto= len(inventario)

    print(f"\nel valor total del inventario es: {valor_total}")
    print(f"el cantidad total de productos registrados es: {total_producto}\n")