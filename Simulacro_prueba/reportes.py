import csv

#cargar equipos

def cargar_equipos():
    equipos=[]
    try:
        with open("equipos.csv", mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                equipos.append(fila)
    except FileNotFoundError:
        print("El archivo equipos.csv no existe todavía")
    return equipos

#cargar prestamos

def cargar_prestamos():
    prestamos=[]
    try:
        with open("prestamos.csv", mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                prestamos.append(fila)
    except FileNotFoundError:
        print("El archivo prestamos.csv no existe todavía")
    return prestamos

#reporte 1: equipos disponibles

def reporte_equipos_disponibles():
    print("\n---------------REPORTE DE EQUIPOS DISPONIBLES----------------\n")
    equipos=cargar_equipos()
    
    disponibles= [e for e in equipos if e["estado_actual"]== "DISPONIBLE"]

    if not disponibles:
        print("\nNo hay equipos disponibles\n")
        return
    
    for e in disponibles:
        print(f"ID: {e['equipo_id']} | Nombre: {e['nombre_equipo']} | Categoria: {e['categoria']} | fecha: {e['fecha_registro']}")

#reporte 2: equipos prestados

def reporte_equipos_prestados():
    print("\n------REPORTE EQUIPOS PRESTADOS----------\n")
    prestamos=cargar_prestamos()

    if not prestamos:
        print("No hay prestamos disponibles\n")
        return
    
    for p in prestamos:
        print(f"ID prestamo: {p['prestamo_id']} | Equipo: {p['equipo_id']} | Cliente: {p['cliente']} | Fecha: {p['fecha_prestamo']}")

#reporte 3: equipo por categoria

def reporte_por_categoria():
    print("\n----REPORTE EQUIPOS CATEGORIA-------\n")
    equipos= cargar_equipos()

    if not equipos:
        print("\nNo hay equipo registrado\n")
        return
    
    categoria=input("\nIngrese la categoria a consultar: ")

    filtrados=[e for e in equipos if e['categoria'].lower() ==categoria.lower()]

    if not filtrados:
        print(f"\nNo existen equipos de la categoria '{categoria}'")
        return
    for e in filtrados:
        print(f"ID: {e['equipo_id']} | Nombre: {e['nombre_equipo']} | Estado: {e['estado_actual']} | Fecha: {e['fecha_registro']}")

def reporte_historial_prestamos():
    print("\n--------- HISTORIAL DE PRÉSTAMOS ---------\n")
    prestamos = cargar_prestamos()

    if not prestamos:
        print("No hay préstamos registrados.\n")
        return

    for p in prestamos:
        print(
            f"ID Préstamo: {p['prestamo_id']} | "
            f"Equipo: {p['equipo_id']} | "
            f"Cliente: {p['cliente']} | "
            f"Fecha préstamo: {p['fecha_prestamo']} | "
            f"Fecha devolución: {p.get('fecha_devolucion', '---')}"
        )