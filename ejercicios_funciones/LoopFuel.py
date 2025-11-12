# 16. Gasolinera “LoopFuel” – Control de litros vendidos
# Como operador, quiero usar un while que sume litros hasta superar 100.
# Cada vez que se venda una cantidad, verificar:

gasolina=0

while gasolina <= 100:
    litros=int(input("Cuantos litros quiere"))
    gasolina += litros
    print(f"usted acaba de vender {gasolina}")
    
print(f"usted cumplio la meta y vendio {gasolina}")
