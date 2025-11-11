# 6. Fábrica “LoopTech” – Control de producción
# Como supervisor, quiero que un for muestre los productos fabricados del 1 al número que indique el usuario.
# Si el número es par, mostrar “Producto verificado”.
# Si es impar, mostrar “Producto pendiente”.
contador= 1
usuario= int(input("Ingrese cuantos productos necesita"))
for i in range(contador, usuario+1):
    if contador % 2 ==0:
        print(f"{i} producto verificado")
    else:
        print(f"{i} producto pendiente")
    contador += 1 