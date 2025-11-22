import csv
from datetime import datetime
from equipos import cargar_equipos  #para verificar disponibilidad
from equipos import listar_equipos  #para mostrar equipos si se requiere 

#cargar prestamos 

def cargar_prestamos():
    prestamos=[]
    try:
        with open("prestamos.csv", mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                prestamos.append(fila)

    except FileNotFoundError:
        print("El archivo prestamos.csv no existe todavia")
    return prestamos

#guardar un prestamo nuevo

