import csv

def guardar(inventario, nombre_archivo="inventario.csv"):
#     "w" → modo escritura sobrescribe el archivo si ya existe.

# newline="" → evita líneas en blanco extra en Windows.

# encoding="utf-8" → permite caracteres como tildes.
    try:
        with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
            columnas = ["nombre", "precio", "cantidad"]
            writer = csv.DictWriter(archivo, fieldnames=columnas)
            writer.writeheader() #writer.writeheader()
            writer.writerows(inventario)#Cada diccionario del inventario se convierte en una fila CSV.
    # DictWriter permite escribir diccionarios en formato CSV.
    # fieldnames indica el orden de las columnas.
        print("Inventario exportado correctamente.")

    except Exception as e:
        print("Error al exportar CSV:", e)


def cargar(nombre_archivo="inventario.csv"):#Intenta leer el archivo CSV y convertirlo nuevamente a una lista de diccionarios.
    
    inventario = []
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            reader = csv.DictReader(archivo) #Cada fila se convierte automáticamente en un diccionario.
            
            for fila in reader:
                inventario.append({
                    "nombre": fila["nombre"].lower(),
                    "precio": float(fila["precio"]),
                    "cantidad": int(fila["cantidad"])
                })

        print("Inventario cargado correctamente.")
        return inventario

    except FileNotFoundError:
        print("El archivo no existe, se creará cuando exportes.")
        return []

    except Exception as e:
        print("Error al cargar CSV:", e)
        return []