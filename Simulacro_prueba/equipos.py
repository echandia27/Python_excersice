import csv
from datetime import date

def cargar_equipos():
    equipos=[]
    try:
        with open("equipos.csv",mode="r", newline="", encoding="utf-8") as archivo:
            lector= csv.DictReader(archivo)
            for fila in lector:
                equipos.append(fila)
    except FileNotFoundError:
        print("El archivo equipos.csv, no existe todavia")
    return equipos

def registrar_equipo():
    print("\n-----REGISTRO DEL EQUIPO-----\n")
    
    equipo_id= input("ID del Equipo: ")
    nombre= input("Nombre del Equipo: ")
    categoria= input("Categoria: ")
    
    fecha_registro= str(date.today())
    estado="DISPONIBLE"

    with open("equipos.csv", mode="a", newline="", encoding="utf-8",) as archivo:
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

#listar equipos
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
