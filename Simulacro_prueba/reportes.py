import csv

def formatear_fecha(fecha):
    """Convierte AAAAMMDD a AAAA-MM-DD"""
    if len(fecha) == 8:
        return f"{fecha[0:4]}-{fecha[4:6]}-{fecha[6:8]}"
    return fecha

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
        print(f"ID prestamo: {p['prestamo_id']} | Equipo: {p['equipo_id']} | Usuario: {p['usuario_prestatario']} | Fecha: {formatear_fecha(p['fecha_prestamo'])}")

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
            f"Usuario: {p['usuario_prestatario']} | "
            f"Fecha préstamo: {formatear_fecha(p['fecha_prestamo'])} | "
            f"Fecha devolución: {formatear_fecha(p.get('fecha_devolucion', '---'))}"
        )