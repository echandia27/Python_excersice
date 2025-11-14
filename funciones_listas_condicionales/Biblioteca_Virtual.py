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

def agregar(libros):
    libro=str(input("Agregue nombre de libro"))
    
