# 1. Sistema de Biblioteca Virtual

# Descripción:
# Crea un programa que permita gestionar una pequeña biblioteca.

# Debe permitir:

#     Ver los libros disponibles.
#     Agregar nuevos libros.
#     Prestar libros (cambiar su estado a “prestado”).
#     Devolver libros.
#     Ver el historial de préstamos.

libros_inventario=[]

historial=[]

def ver():
    print("Libros Disponibles")
    for libro in libros_inventario:
        if libro ["estado"] == "disponible":
            print(f"- {libro ['titulo']}\n")



def agregar():
    titulo=str(input("Agregue nombre de libro\n"))
    libros_inventario.append({"titulo":titulo, "estado":"disponible"})
    print("Libro agregado\n")

def prestar():
    titulo=str(input("Ingrese el titulo que desea prestar\n"))

    for libro in libros_inventario:
        if libro["titulo"].lower() == titulo.lower():
            if libro["estado"] == "disponible":
                libro["estado"] = "prestado"
                historial.append(f"se presto:{libro['titulo']}")
                print("Libro prestado\n")
                return
            else:
                print("Este libro ya esta prestado\n")

    print("libro no existe\n")

def devolver():
    titulo=str(input("Agregue nombre de libro a devolver\n"))

    for libro in libros_inventario:
        if libro["titulo"].lower() == titulo.lower():
            if libro["estado"] == "prestado":
                libro["estado"] = "disponible"
                historial.append(f"se entrego:{libro['titulo']}")
                print("Libro entregado\n")
                return
            else:
                print("Este libro no esta prestado")

    print("Libro no existe\n")

def historiales():
    print("<----- Historial de prestamos ----->")
    for prestamo in historial:
        print("- " + prestamo )
    
while True:
    print("\n<------Biblioteca Virtual------>")
    print("1. Ver libros disponibles")
    print("2. Agregar nuevos libros")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Ver historial")
    print("6. Salir\n")
    
    try:
        opcion=int(input("Ingresa el número de lo que deseas hacer\n"))
    except ValueError:
        print("Debes ingresar números")
        continue

    
    if opcion ==1:
        ver()
        
    elif opcion == 2:
        agregar()

    elif opcion == 3:
        prestar()

    elif opcion == 4:
        devolver()

    elif opcion == 5:
        historiales()

    elif opcion == 6:
        print("Sesión Terminada\n")
        break

    else:
        print("Opcion invalida Intente de nuevo\n")
        



