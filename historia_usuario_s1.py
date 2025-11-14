# 1. Diagrama de flujo inicial:

#     Diseña un diagrama de flujo que represente el proceso de registrar un producto en el inventario.
#     Debe incluir los pasos: Inicio → Leer nombre, precio y cantidad → Calcular costo total → Mostrar resultado → Fin.
#     Realízalo en draw.io y guarda la evidencia como imagen o PDF.

# TASK 2
# 2. Entrada de datos (variables en Python):

#     Crea un archivo inventario.py.
#     Declara variables para nombre (string), precio (float) y cantidad (int).
#     Solicita al usuario estos datos con la función input().
#     Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
#     Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.


# Aqui se  van a solicitar los datos
producto=str(input("Ingresa el nombre "))
precio=float(input("Ingresa el precio "))
if precio <= 0:
    print("Valor invalido")
    precio=float(input("Ingresa el precio "))
cantidad=int(input("Ingresa la cantidad "))
if cantidad <= 0:
    print("Valor invalido")
    cantidad=int(input("Ingresa la cantidad "))

# TASK 3
# 3. Operación matemática (costo total):

#     Crea una variable llamada costo_total.
#     Almacena en ella el resultado de multiplicar el precio por la cantidad (precio * cantidad).
#     Asegúrate de que la operación se realice después de validar los datos de entrada.

#se crea un variable para solicitar el total del producto
def costo_total():
    total= precio * cantidad
    return total

print(costo_total())

# TASK 4
# 4. Mostrar resultados en consola:

#     Usa la función print() para mostrar un mensaje con:
#         Nombre del producto
#         Precio unitario
#         Cantidad
#         Costo total calculado
#     El formato del mensaje debe ser claro, por ejemplo: "Producto: Lápiz | Precio: 500 | Cantidad: 3 | Total: 1500"

#se hace la impresion verificando que todo este correcto
print(f"Producto:{producto} | Precio:{precio} | Cantidad:{cantidad} | Total: {costo_total()} ")


# TASK 5
# 4. Documentación del código:

#     Incluye comentarios (#) antes de cada bloque de código explicando qué hace.
#         Ejemplo: # Solicitar datos al usuario
#         nombre = input("Ingrese el nombre del producto: ")
#     Al final del archivo, escribe un comentario general explicando qué hace el programa completo.

'''este programa es un inventario que recibirar el nombre del producto el precio y la cantidad y al final te imprime todo junto al costo total '''


