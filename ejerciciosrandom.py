#Crea una lista con 5 nombres de tus amigos y muestra el segundo y el último.

#Crea una lista con 5 números y muestra la suma de todos.

#Agrega un nuevo número al final de la lista y vuelve a mostrarla.

#Elimina el primer elemento de la lista.

#Ordena la lista de menor a mayor.

'''
personas = ["pedro", "juan", "camilo", "santiago", "alonso"]
print(personas[2] )

numeros = [1, 5, 7, 8, 15]
suma=sum(numeros)
print(suma)


numeros.append(27)

print(numeros)

del numeros[0]
print(numeros)


numeros.reverse()
print(numeros)
personas.reverse()
print(personas) '''

numeros = []

for i in range (10):
    n= int(input("Ingrese 10 números"))
    numeros.append(n)

print("de mayor ", max(numeros))
print("de menor ", min(numeros))
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)