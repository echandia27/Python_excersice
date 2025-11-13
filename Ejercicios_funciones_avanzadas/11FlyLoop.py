# 11. Aerolínea “FlyLoop” – Cálculo de millas acumuladas
# Como viajero frecuente, quiero una función calcular_millas(viajes) que reciba el número de viajes realizados y sume millas según la distancia:

#     Viaje corto (< 1000 km): 500 millas
#     Medio (1000–3000 km): 1000 millas
#     Largo (> 3000 km): 2000 millas
#     Debe repetirse hasta que el usuario escriba “fin” y mostrar el total acumulado.

def calcular_millas():
    acumulado=0
    viajes=1
    while True:
        sumarmillas= input("Ingrese distancia ")
        if sumarmillas.lower() == "fin":
            break
        sumarmillas=int(sumarmillas)

        if sumarmillas < 1000:
            print(f"viaje {viajes} corto sumo 500 millas")
            acumulado+=500
        elif sumarmillas >= 1000 and sumarmillas <= 3000:
            print(f"viaje {viajes} medio sumo 1000 millas")
            acumulado+=1000
        else:
            print(f"viaje {viajes} largo sumo 2000 millas")
            acumulado+=2000
        viajes+=1
    print(f"total millas acumulado {acumulado}")
    
calcular_millas()

    
            

            

    
    

