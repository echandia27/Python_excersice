# 2. Cine “La Estrella” – Cuenta regresiva antes de iniciar la función
# Como proyeccionista, quiero mostrar una cuenta regresiva del 5 al 1 usando for. Si llega al número 1, debe imprimir “¡Que empiece la función!”.

for i in range (5,0,-1):
    if i == 1:
        print(f"{i}¡Que empiece la función!")
    else:
        print(f"{i}")