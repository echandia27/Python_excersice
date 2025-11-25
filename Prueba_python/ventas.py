from datetime import date, datetime

comprador=[]

def libro_vendido(library):
    hora=datetime.now()
    print("\nWhich book are you interested in buying?")
    try: 
        libro_interesado=str(input("Enter the name of the book you want to buy: "))
    except ValueError:
        print("Enter a valid name")

    for libro in library:
        if libro["book"] == libro_interesado:
            print("\nProduct found")
            print(libro)
            precio_libro=int(libro['precio'])
            libros_stock=int(libro['stock'])

            try: 
                cuantos=int(input("Enter how many books you want: "))
            except ValueError:
                print("Enter a valid integer")
            

            if cuantos > libros_stock:
                print("\nThere is not enough stock")
                return libros_stock
                    

            libros_stock -= cuantos
            libro["stock"] =libros_stock

            valor_libro= cuantos * precio_libro
            if valor_libro >= 20000:
                valor_libro= valor_libro* 0.80
                print(f"You have purchased more than 20,000 and have received a 20% discount. Total to pay: {valor_libro} - Date: {hora} ")    
            print(f"total to pay{valor_libro}\n")
            compra  = {
                "book":libro["book"],
                "autor":libro["autor"],
                "categoria":libro["categoria"],
                "precio":valor_libro,
                "stock":cuantos,
            }

            comprador.append(compra)

def reportes(comprador):

    top3= max(comprador, key=lambda p: p["stock"])
    valor_total = sum(p["precio"] * p["stock"] for p in comprador)


    while True:
        print("===REPORTS MENU===")
        print("1. Show top3 best selling products")
        print("2. Generate a report of total sales grouped by author.")
        print("3. Calculate net and gross income (with and without discount)")
        print("4. Return previous menu")

        try:
            opcion=int(input("Enter the number of where you want to go: "))
            if opcion <= 0 or opcion >= 9:
                print("Enter a number between the parameters")

            elif opcion == 1:
                print(f"The best-selling product is: {top3}")
            
        
            elif opcion == 3:
                print(f"The total value sold is: {valor_total}")

            elif opcion == 2:
                try:
                    escoger_autor=str(input("Which author are you looking for? "))
                except ValueError:
                    print("Enter what is requested")
                total_autor=sum(p["precio"]* p["stock"] for p in comprador if p["autor"]== escoger_autor)
                print(f"The total cost of sale {escoger_autor} is {total_autor}")
   
            elif opcion == 4:
                print("\n Back to the previous menu")
                break
        
            else:
                print("\Invalid option, please try again.\n")
                
        except ValueError:
            print("Enter an integer")






            
            




