
#sumatoria de los numeros de 1 al 10
'''suma = 0
for i in range (1,11):
    suma += i
print("la suma de los 10 primeros digitos es",suma)'''

# cuenta regresiva del 10 al 1

'''for i in range (10,0, -1):
 print(i)'''

#promedio factorial

'''n=int(input("Ingrese un número:"))
factorial=1
for i in range(1,n+1):
    factorial *= i
print(f"El factorial de {n} es {factorial}")'''

# promedio de calificaciones

'''nota1=float(input( "agregue la primera nota " ))
nota2=float(input( "Agregue su segunda nota " ))
nota3=float(input( "agregue su tercera nota " ))

promedio = (nota1 + nota2 + nota3) / 3
if promedio >= 3:
    print(f"Usted aprobo y su nota es: {promedio}")
else:
    print(f"Usted reprobo y su nota es: {promedio}")'''

#bucle de numero con par o impar

'''numero = int(input("escriba el numero " ))

for i in range (numero+1):
    if i % 2 ==0:
        print(f"El numero {i} es PAR")
    else:
        print(f"El numero {i} es IMPAR")'''


lineas= int(input("inserte numero de lineas "))


print("Bellow is the triangle pattern")

for i in range(1,lineas+1):
    espacios = " " * (lineas - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

#     # ahora la formula para invertirlo
    
for i in range(lineas-1, -1, -1):
    espacios = " " * (lineas - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)





























     


