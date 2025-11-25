import libros
import ventas

# • Cada producto debe tener: título, autor, categoría, precio, cantidad en stock.
library=[
    {"book":"Harry Potter", "autor":"jorge", "categoria":"fantasia", "precio":"10000", "stock":"5"},
    {"book":"narnia", "autor":"francisco", "categoria":"fantasia", "precio":"8000", "stock":"3" },
    {"book":"el mundo", "autor":"pedro", "categoria":"geografia", "precio":"7000", "stock":"7"},
    {"book":"paisajes", "autor":"maria", "categoria":"arte", "precio":"5000", "stock":"4"},
    {"book":"cuerpo humano", "autor":"juan", "categoria":"anatomia", "precio":"3000", "stock":"10"},

]



while True:
    print("----National Bookstore----")
    print("1. ADD Book")
    print("2. Show books")
    print("3. Search ")
    print("5. Delete Book ")
    print("6. Sales ")
    print("7. Reports module")
    print("8. Exit")

    try:
        opcion=int(input("Enter the number of where you want to go: "))
        if opcion <= 0 or opcion >= 9:
            print("Enter a number between the parameters")
    
    

        elif opcion == 1:
            libros.add_book(library)
        
        elif opcion == 2:
            libros.mostrar(library)
            

        elif opcion == 3:
            libros.buscar(library)

        elif opcion == 4:
             libros.actualizar(library)

        elif opcion == 5:
            libros.Eliminar_producto(library)

        elif opcion == 6:
            ventas.libro_vendido(library)

        elif opcion ==7:
            ventas.reportes(ventas.comprador)
                

        elif opcion ==8:
            print("see you tomorrow!")
            break
        else:
            print("\nInvalid option, please try again\n")
                
    except ValueError:
        print("Enter a number between the parameters")


