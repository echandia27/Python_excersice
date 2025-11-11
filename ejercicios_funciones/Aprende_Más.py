# 5. Escuela “Aprende Más” – Registro de tareas entregadas
# Como profesor, quiero usar un while que sume tareas hasta 10. Si el contador llega a 10, mostrar 
# “¡Todas las tareas recibidas!”. Si aún no llega, mostrar cuántas faltan.
tarea= 1
contador= 10
while tarea < contador:
    print(f"te faltan {contador - tarea} por recibir")
    tarea += 1
else:
    print("¡Todas las tareas recibidas!")
    