# 13. Tienda Online “ShopMaster” – Carrito de compras con validaciones
# Como comprador, quiero una función carrito() que permita ingresar precios de productos y valide:

#     Si el precio es negativo, mostrar error y pedir otro valor.
#     Si el precio es mayor a 100.000, aplicar un 20% de descuento.
#     Usar while y if dentro de la función hasta ingresar 0 para finalizar.

def carrito():
    suma=0
    while True:
        precio=int(input("Ingrese precio de producto "))
        if precio ==0:
            break
        elif precio < 0:
            print("Error Ingrese otro valor")
        elif precio > 100000:
            precio= precio * 0.80
            print(f"el valor del producto {precio} ")
            suma+=precio
        else:
            print(f"el valor del producto {precio} ")
            suma+=precio
    return suma
mercado=carrito()
print(f"total es {mercado}")
