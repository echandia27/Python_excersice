# 13. Parqueadero “AutoLoop” – Control de vehículos
# Como vigilante, quiero usar un while que cuente vehículos hasta llegar a 20.
# Si entra un número par, mostrar “Vehículo par registrado”.
# Si el total llega a 20, mostrar “Capacidad completa”.

vehiculos= 1
while  vehiculos <= 20:
    if vehiculos % 2 ==0:
        print(f"{vehiculos} Vehículo par registrado")
    else:
        print(f"{vehiculos} Vehículo inpar registrado")

    vehiculos += 1
   
print("Capacidad completa")