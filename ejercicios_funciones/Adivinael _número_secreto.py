# 9. Concurso “Adivina el número secreto”
# Como participante, quiero que el programa me pida un número entre 1 y 5 usando un while.
# Si acierto, mostrar “¡Correcto!”.
# Si no, mostrar “Intenta otra vez” y seguir hasta acertar.

secreto= 3
numero=int(input("Ingresa un numero del 1 al 5 "))
while numero != secreto:
    while numero < 1 or numero > 5:
        print("numero fuera de rango")
        numero=int(input("Ingresa un numero del 1 al 5 "))
    
    if numero != secreto:
        numero=int(input("Ingresa un numero del 1 al 5 "))

print("!Correcto¡")
            
    
        