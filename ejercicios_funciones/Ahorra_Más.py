# 14. Tienda “Ahorra Más” – Caja registradora básica
# Como cajero, quiero pedir montos de venta hasta que el usuario escriba 0.
# Si la venta supera $100,000, mostrar “Venta destacada”.
# Al final, mostrar el total vendido.

monto= 0

venta=int(input("Ingrese monto "))
while venta != 0:
    venta=int(input("Ingrese monto "))
    monto += venta
    if monto > 100000:
        print("venta destacada")
print(f"total vendido {monto}")
