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
    try:
        usuario= input("Nombre del usuario prestatario: ")
        tipo= (input("tipo de usuario (ESTUDIANTE / INTRUCTOR / ADMINITRATIVO): ")).upper()
    except ValueError:
        print("ingresa un valor correcto")

    if tipo not in ("ESTUDIANTE", "INTRUCTOR", "ADMINISTRATIVO"):
        print("Tipo de Usuario invalido")
        return
    
    #fechas y dias
    try:
        fecha_prestamo= input("fecha del prestamo (YYYY-MM-DD): ")
        dias= (input("Dias solicitados"))
    except ValueError:
        print("ingresa un valor correcto")

    #limites

    limites={"ESTUDIANTE": 3, "INTRUCTOR": 7, "ADMINISTRATIVO": 10 }

    if dias > limites[tipo]:
        print(f"Este usuario solo puede pedir {limites[tipo]} dias")
        return
    
    hoy=datetime.today()
    prestamo_id=generar_id()

    nuevo_prestamo= {
        "prestamo_id": prestamo_id,
        "equipo_id": equipo['equipo_id'],
        "nombre_equipo": equipo["nombre_equipo"],
        "usuario_prestatario": usuario,
        "tipo_usuario": tipo,
        "fecha_solicitud": str(hoy.date()),
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": "",
        "dias_autorizados": dias,
        "dias_reales_usados": "",
        "retraso": "",
        "estado": "PENDIENTE",
        "mes": hoy.month,
        "anio": hoy.year
    }

    guardar_prestamo(nuevo_prestamo)

    print("\n====Solicitud guardada como PENDIENTE\====n")

    #listar prestamo

def listar_prestamo():
    print("\n----------Lista de prestamos-----------\n")

    prestamos= cargar_prestamos()

    if not prestamos:
        print("\nNo hay prestanis registrados\n")
        return
    for p in prestamos:
        print(f"{p['prestamo_id']} | Equipo: {p['nombre_equipo']} |"
                f"{p['usuario_prestatario']} | Estado: {p['estado']}")
            
    #aprobar, rechazar prestamo

def aprobar_prestamo():
    prestamos= cargar_prestamos()
    pendientes=[p for p in prestamos if p["estado"]== "PENDIENTE"]

    if not pendientes:
        print("\nNo hay solicitudes pendientes")
        return
    print("\nPrestamos Pendientes\n")
    for p in pendientes:
        print(f"{p['prestamo_id']}-{p['nombre_equipo']}")

    try:
        id_buscar= input("\nID del prestamo a aprobar/rechazar: ")
    except ValueError:
        print("Ingrese aprobar o rechazar")

    for p in prestamos:
        if p["prestamo_id"] == id_buscar:
            decicion= input("\nAprobar unda (A) de lo contrario sera recahzado").upper()

            if decicion =="A":
                p["estado"]= "APROBADO"
                print("\nPrestamo: APROBADO")
            else:
                p["estado"]= "RECHAZADO"
                print("\nPrestamo: RECHAZADO")

            #guardar cambios    
            sobreescribir_prestamos(prestamos)
            return
    print("\nNo se encontro ID\n")

#sobre escribir archivo con prestamo actualizado

def sobreescribir_prestamos(lista):








