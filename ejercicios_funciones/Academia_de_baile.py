# 8. Academia de baile – Calentamiento previo
# Como instructor, quiero usar un while para contar del 1 al 5.
# Si el número es menor que 5, mostrar “Sigue calentando...”, y si llega a 5, mostrar “¡Listo para bailar!”.

for i in range(5):
    while i == 4:
        print("¡Listo para bailar!")
        break
    else:
        print("Sigue calentando...")