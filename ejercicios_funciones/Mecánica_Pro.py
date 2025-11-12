# 10. Taller “Mecánica Pro” – Revisiones del día
# Como mecánico, quiero usar un for que muestre “Revisión X”.
# Si X es igual a 3, mostrar “Revisión especial de motor”.

for i in range(1,4):
    if i == 3:
        print("Revisión especial de motor")
    else:
        print(f"Revisión {i}")