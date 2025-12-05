lista=[ 1,5,3,9,2]
def numero_mas_alto(lista):
    if not lista:
        return None
    mas_alto = 0
    for numero in lista:
        if numero > mas_alto:
            mas_alto = numero
    return mas_alto 
print(numero_mas_alto(lista))
print(max(lista))

# palindromo

palabra=input("ingrese palabra: ")

if palabra == palabra [::-1]:
    print("es palidromo")
else:
    print("no es palidromo")

# fizzbuzz

numero=int(input("ingrese un numero:"))
for i in range(1, numero +1):
    if i % 3 == 0 and i % 5 == 0: 
        print("fizzbuzz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0:
        print("fizz")
    else:
        print(i)   


