# 3. Tienda “LoopShop” – Descuentos acumulados
# Como vendedor, quiero una función aplicar_descuentos() que pida varios precios hasta que el usuario escriba 0.
# Si el precio supera 50.000, aplicar 10% de descuento.
# Al final, mostrar la suma total de las compras con descuento.



def aplicar_descuentos():
    precios=0
    precio=-1
    while precio != 0:
        precio=int(input("Introducir precio "))
        if precio == 0:
           break
        if precio > 50000:
         total= precio * 0.90
         
      
        else:
           total= precio
        precios += total
    return precios
        

print(f"la suma total {aplicar_descuentos()} ")
         
