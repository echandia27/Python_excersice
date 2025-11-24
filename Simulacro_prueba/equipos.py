import csv
from datetime import date
import os

ruta_actual = os.path.dirname(os.path.abspath(__file__))
archivo_equipos = os.path.join(ruta_actual, "equipos.csv")

def cargar_equipos():
    equipos=[]
    try:
        with open(archivo_equipos,mode="r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
            for fila in lector:
                equipos.append(fila)
    except FileNotFoundError:
        print("El archivo equipos.csv, no existe todavia")
    return equipos

def guardar_equipos(equipos):
    with open(archivo_equipos, mode="w", newline="", encoding="utf-8") as archivo:
        campos = ["equipo_id", "nombre_equipo", "categoria", "estado_actual", "fecha_registro"]
        writer = csv.DictWriter(archivo, fieldnames=campos)
        writer.writeheader()
        writer.writerows(equipos)

def registrar_equipo():
    print("\n-----REGISTRO DEL EQUIPO-----\n")
    
    equipo_id= input("ID del Equipo: ")
    nombre= input("Nombre del Equipo: ")
    categoria= input("Categoria: ")
    
    fecha_registro= str(date.today())
    estado="DISPONIBLE"

    with open(archivo_equipos, mode="a", newline="", encoding="utf-8",) as archivo:
        campos=["equipo_id", "nombre_equipo", "categoria", "estado_actual", "fecha_registro"]
        escritor= csv.DictWriter(archivo, fieldnames=campos)

#escribir encabezado si el archivo esta vacio
        if archivo.tell() == 0:
            escritor.writeheader()

        escritor.writerow({
            "equipo_id":equipo_id,
            "nombre_equipo":nombre,
            "categoria":categoria,
            "estado_actual":estado,
            "fecha_registro":fecha_registro,
        })

        print("\nEquipo registrado exitosamente")

#mostrar equipos
def listar_equipos():
    print("\n-----LISTAR EQUIPOS-----")

    equipos=cargar_equipos()

    if not equipos:
        print("\nNo hay equipos registrados")
        return
    for equipo in equipos:
        print(f"\nID: {equipo['equipo_id']} |"
              f"nombre del equipo: {equipo['nombre_equipo']} |"
              f"Categoria: {equipo['categoria']} |"
              f"El estado actual del equipo es:{equipo['estado_actual']} |"
              f"Fecha: {equipo['fecha_registro']}\n"
              )

def consultar_equipo():
    print("----CONSULTA DEL EQUIPO----")

    equipo_id=input("Ingrese el id del equipo: ")
    equipos=cargar_equipos()

    for e in equipos:
        if e["equipo_id"]==equipo_id:
            print("\nInformacion del equipo: ")
            print(f"ID: {e['equipo_id']}")
            print(f"Nombre: {e['nombre_equipo']}")
            print(f"Categoria: {e['categoria']}")
            print(f"Estado: {e['estado_actual']}")
            print(f"Fecha de registro: {e['fecha_registro']}")
            return
        
    print("No se encontro ningun equipo con esa ID")

def poner_en_mantenimiento():
    equipos=cargar_equipos()
    equipo_id=input("Ingrese el ID del equipo que se ira a mantenimiento: ")

    equipo= next((e for e in equipos if e ["equipo_id"] == equipo_id), None)

    if not equipo:
        print("Equipo no encontrado.")
        return
    equipo["estado_actual"]= "MANTENIMIENTO"

    guardar_equipos(equipos)
    print("\nEquipo puesto en mantenimiento")

def quitar_de_mantenimiento():
    equipos = cargar_equipos()
    equipo_id = input("Ingrese el ID del equipo: ")

    equipo = next((e for e in equipos if e["equipo_id"] == equipo_id), None)

    if not equipo:
        print("Equipo no encontrado.")
        return

    equipo["estado_actual"] = "DISPONIBLE"

    guardar_equipos(equipos)
    print("Equipo habilitado nuevamente.")
