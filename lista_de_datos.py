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

#eliminar por posicion

lista = [10, 20, 30, 40]
eliminado = lista.pop(2)

print(lista)      # [10, 20, 40]
print(eliminado)  # 30

#generar un id automatico empezando desde el 1, 2 , 3 y asi
def generar_id_automatico(productos):
    if not productos:
        return 1
    ultimo_id = max(p["id"] for p in productos)
    return ultimo_id + 1