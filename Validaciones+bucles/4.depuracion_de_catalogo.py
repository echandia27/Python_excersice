# 4) Biblioteca “Depuración de catálogo” — Eliminar libro específico
# Como bibliotecario, quiero una función eliminar_libro(catalogo, titulo) que verifique si el título está y lo quite.

# Si no existe, mostrar “no encontrado”.
# Imprimir los libros restantes con un bucle.
# Sugerencia: usa list.remove().

libros=[
    {"titulo":"harry potter"}, 
    {"titulo":"narnia" }
    ]

def eliminar():
    libro=str(input("Ingrese nombre del libro "))

    encontrado=False
    for i in libros:
        if i["titulo"].lower() == libro.lower():
            libros.remove(i)
            print(f"libro eliminado correctamente")
            encontrado=True
            break
    if not encontrado:
            print("EL libro no se encuentra")
    print("Lista actualizada")
    for i in libros:
        print(f"- {i['titulo']} ")

eliminar()

