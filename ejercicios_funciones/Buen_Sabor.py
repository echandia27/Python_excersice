# 7. Restaurante “Buen Sabor” – Revisión de limpieza
# Como jefe de cocina, quiero usar un for para repetir 3 veces el mensaje “Limpia tu estación”.
# Si es la última vez, mostrar “¡Revisión completada!”.

for i in range(4):
    if i == 3:
        print("¡Revisión completada!")
    else:
        print("Limpia tu estación")