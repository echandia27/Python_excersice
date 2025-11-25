

def add_book(library):
    print("----ADD NEW BOOK----")
    try:
        name_book=str(input("Add name book: "))
        #Check if the product already exists
        for libro in library :
            if libro["book"].lower()== name_book.lower():#.lower es para que sea minisculas
                print("Product already exists, quantity will be added\n")

                while True:
                    try:
                        cantidad= int(input("Enter the amount to add: "))
                        if cantidad <=0:
                            print("Invalid value, must be greater than 0")
                            continue
                        break
                    except ValueError:
                        print("Enter a valid integer")
                libro["stock"]=int(libro["stock"]) + cantidad
                print("The amount was added\n")
                return
        # como el producto no existe se crea 
        try:
            autor=str(input("Enter book author: "))
        except ValueError:
            print("Enter a valid parameter\n")
            

    
        try:
            categoria=str(input("Enter book category: "))
        except ValueError:
            print("Enter a valid parameter\n")
        
        while True:
            try:
                precio=int(input("Enter the product price: "))
                if precio <= 0:
                    print("enter a positive value")
                    continue
                break
            except ValueError:
                print("Enter a valid number")
        
        while True:
            try:
                stock=int(input("Enter the product stock: "))
                if precio <= 0:
                    print("enter a positive value")
                    continue
                break
            except ValueError:
                print("Enter a valid number")

        
        nuevo_book= {
            "book": name_book,
            "autor": autor,
            "categoria": categoria,
            "precio":precio,
            "stock":stock
        }

        library.append(nuevo_book)
        print("\nEl producto fue agregado correctamente\n")

    except Exception as e:
        print(f"Error Inesperado {e}\n") #se empieza con un try y lo que hace es que no salga un error
                                        #indesperado en la funcion

#mostrar todos los libros

def mostrar(library):
        if not library:
            print("\n<------El inventario esta vacio------->\n")
            return
        for libro in library:
            print(f"book:{libro['book']} author:{libro['autor']} category:{libro['categoria']} price:{libro['precio']} stock:{libro['stock']}\n")

#buscar un libro en especifico

def buscar(library):
    buscando=str(input("Ingrese el nombre del producto a buscar: "))
    for libro in library:
        if buscando == libro["book"]:
            print(f"book:{libro['book']} author:{libro['autor']} category:{libro['categoria']} price:{libro['precio']} stock:{libro['stock']}\n")

#actualizar libro

def actualizar(library):
    if not library:
        print("\nEmpty inventory")
        return
    try:
        actualizar_libro=str(input("Enter the name of the book to update: "))
    except ValueError:
        print ("Enter a product name")

    for libro in library:
        if libro["book"] == actualizar_libro:
            print("\nProduct found")
            print(libro)

            print("\n What do you want to update?")
            print("1. Author")
            print("2. Category")
            print("3. Price")
            print("4. Stock")

            try:
                opcion=int(input("Enter the option you wish to choose: "))

                if opcion == 1:
                    libro["autor"]= input("New author: ")
                elif opcion == 2:
                    libro["categoria"]= input("Enter a new category: ")
                elif opcion == 3:
                    libro["precio"]= int(input("Enter new price: "))
                elif opcion == 4:
                    libro["stock"]= int(input("New stock added: "))
                
                else:
                    print("Invalid option\n")
            except ValueError:
                print("Enter a valid parameter\n")
    print(f"\n{libro}\n")

#delete book
def Eliminar_producto(library):
    try:
        eliminar=str(input("Enter the name of the book you want to delete\n"))
    except ValueError:
        print("Enter a valid parameter")
        return
    for libro in library:
        if libro["book"]== eliminar:
            library.remove(libro)
            print("\nProduct Successfully Removed\n")
            return

    print("\nProduct not found\n")
