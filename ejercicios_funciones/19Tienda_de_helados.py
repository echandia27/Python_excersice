# 19. Tienda de helados – Registro de clientes atendidos
# Como empleado, quiero usar un while que cuente clientes hasta que el número supere 15.
# Si el número es múltiplo de 5, mostrar “Pausa para limpieza”.
# Al final, mostrar “Turno finalizado”.

turno=1

while turno <16:
    if turno % 5 == 0:
        print("Pausa para limpieza")
    else:
        print(f"cliente numero {turno}")
    turno += 1
print("Turno finalizado")