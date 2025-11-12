lista_nombres = ["Ramiro", "Juan", "Pablo", "Jose"]

for i in lista_nombres:
    while i != "Ramiro":
        print(i)
        break

#otra forma

for i in lista_nombres:
    if i != "Ramiro":
        print(i)
        
#lista vacia

lista_na = []

lista_na.append("Ramiro")
lista_na.append("Pedro")

print(lista_na)

#otro cuidado este tiene un bucle infinito de agregar nombres

'''lista_S = []
while True:

    nombre= input("Ingresa tu nombre ")
    lista_S.append(nombre)
    print(lista_S)'''
    

 #quitar
    
lista_de = ["l", "g", "h", "q"]

lista_de.remove("l")

print(lista_de)
