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

def guardar_prestamo(nuevo):
    campos=[
        "prestamos id", "equipos_id", "nombre_equipo",
        "usuario_prestatario", "tipo_usuario",
        "fecha_solicitud", "fecha_prestamo", "fecha_devolucion",
        "dias_autorizados", "dias_reales_usados",
        "retraso", "estado", "mes", "anio"
    ]

    with open("prestamo.csv", mode="a", newline="",encoding="utf-8") as archivo:
        escritor= csv.DictWriter(archivo, fieldnames=campos)

        if archivo.tell == 0:
            escritor.writeheader()

        escritor.writerow(nuevo)

def generar_id():
    prestamos=cargar_prestamos()
    if not prestamos:
        return "P1"
    
    ultimo= prestamos[-1] [prestamos]
    numero= int(ultimo[1:]) +1
    return f"P{numero}"

#registrar prestamo

def registrar_prestamo():
    print("\n=====Registrar Prestamo=====")
    equipos= cargar_equipos()

    #mostrar solo equipos disponibles
    disponibles=[e for e in equipos if e['estado_actual']== "DISPONIBLE"]
    #esto de abajo es lo mismo que lo de arriba
    ''' disponibles = []
    for e in equipos:
    if e["estado_actual"] == "DISPONIBLE":  
        disponibles.append(e)'''

    if not disponibles:
        print("\n No hay equipos disponibles")
        return
    print("\nEquipos disponibles:")
    for e in disponibles:
        print(f"- {e['equipo_id']} | {e['nombre equipo']} ({e['categoria']})")

    equipo_id= input("\nIngrese id del equipo que desea prestar: ")

    equipo= next((e for e in disponibles if e['equipo_id']== equipo_id), None)

    if equipo is None:
        print("\n No existe un equipo disponible con esa ID")
        return
    
    #datos de prestatario
    





