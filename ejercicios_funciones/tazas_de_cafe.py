# 1. Cafetería “Buen Café” – Control de tazas servidas
# Como barista, quiero usar un bucle for para mostrar cuántas tazas he servido del 1 al 10, pero si el número es 5, 
# mostrar el mensaje “¡Mitad del turno completada!”.

for i in range (1, 11):
    if i < 5 and i > 0:
        print(f"he servido {i} ")
    elif i == 5:
        print(f"he servido {i}  ¡Mitad del turno completada!")
    else:
        print(f"he servido {i} ")

    