'''edad=int(input("Ingrese la Edad"))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("es menor de edad")'''

#1. Panadería de Don Pancho — Descuentos por cantidades

#La panadería de Don Pancho vende pan a $300 cada uno.

#Reglas:

#    Si compra más de 20 panes → 10% descuento
#    Si compra más de 50 panes → 20% descuento
#    Si ingresa una cantidad negativa, mostrar "Cantidad inválida"

#Calcular y mostrar el total.#

'''La panadería de Don Pancho vende pan a $300 cada uno.

Reglas:

    Si compra más de 20 panes → 10% descuento
    Si compra más de 50 panes → 20% descuento
    Si ingresa una cantidad negativa, mostrar "Cantidad inválida"

Calcular y mostrar el total.'''

'''pan=300

cantidad= int(input("cuantos panes quiere "))
precio= pan * cantidad

if cantidad <= 0:
    print(" cantidad invalida")

elif cantidad >= 20:
    print(f" su precio es {precio * 0.90} ")
elif cantidad >= 30:
    print(f" su precio es {precio * 0.80} ")
else:
    print(f" sus panes cuestan {precio} ")'''

#2. Cine “La Estrella” — Tarifas por edad

#Pedir la edad del cliente:
#Edad 	Precio
#< 5 años 	Entrada gratis
#5 a 11 	$5.000
#12 a 59 	$8.000
#≥ 60 	$4.000 (descuento adulto mayor)

#Mostrar el precio.
#Si la edad es negativa, mostrar error.

'''edad= int(input("Deme su edad "))

if edad <= 0:
    print(" Su edad es negativa")
elif edad >= 1 and edad <= 4:
    print(" su entrada es gratis")
elif edad >= 5 and edad <= 11:
    print(" su tarifa es de $5.000")
elif edad >= 12 and edad <= 59:
    print(" su tarifa es de $8.000")
else:
    print("su tarifa es de $4.000")'''

#3. Gimnasio “Solo Leveling Fit” — Motivación + Bono

#Pedir cuántos días entrenó esta semana.

#    ≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
#    2 o 3 → "Bien, pero puedes dar más"
#    0 o 1 → "No aflojes, tú puedes mejorar"

#Mostrar mensaje y si aplica, los puntos ganados.

'''dias= int(input("Cuantos dias entreno "))

if dias == 0 or dias ==1:
    print(" no aflojes, puedes mejorar")
elif dias == 2 or dias == 3:
    print(" Bien, pero puedes dar más")
elif dias >= 4:
    print("¡Excelente Disciplina!")
else:
    print("no aplica")'''

#4. Heladería “Frosty” — Sabor y topping

#Sabores y precios:

#    chocolate → $4.000
#    vainilla → $3.500

#Opcional: topping cuesta $1.000.

#Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
#Si el sabor es válido, preguntar si quiere topping y calcular total.

'''print("que sabor desea, Chocolate = $4000 y Vainilla = $3.500. si adiciona toppin tiene un costo de $1.000")
chocolate = 4000
vainilla = 3500
toppin= 1000
sabor= str(input("escoja que sabor desea "))

if sabor == "chocolate":
    print (f"su costo es de $4.000 ")
    toppin= str(input("desea toppin: si o no "))
    if toppin == " si ":
        print("su costo es $5.000")
    else:
        print("su costo es de $4.000")
elif sabor == "vainilla":
    print (f"su costo es de $4.000 ")
    toppin= str(input("desea toppin: si o no "))
    if toppin == " si ":
        print(" su costo es $4.500")
    else:
        print(" su costo es de $3.500")
else:
    print("sabor incorrecto")'''

#5. Librería “El Saber” — Descuento estudiante + cupón

#Libro cuesta $25.000.

#    Si es estudiante → 15% descuento
#    Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado

#Validar:

#    Si no es estudiante, el cupón no aplica.
#    Si ingresa cupón incorrecto, ignorarlo.

#Mostrar total.

'''libro = 25000

estudiante= str(input(" Es estudiante si o no "))
while estudiante != "si" and estudiante != "no":
    estudiante=str(input("digite si o no "))
if estudiante == "si":
    cupon= str(input("digite el cupón "))
    if cupon == "libro10":
        print(f"El libro le cuesta {libro * 0.75}")
    else:
        print(f"El costo del libro es de {libro * 0.85}")
else:
    print(f"el costo del libro es de {libro} ")'''

#6. Parqueadero “RapidCar” — Tarifa escalonada

#Tarifa:

#    0 a 5 horas: $2.000 x hora

#        5 horas: $2.000 x hora + multa fija de $5.000

#Validar horas:

#    No permitir números negativos.

#Mostrar valor total.

'''hora= 2000
multa= 5000

horas = int(input("Ingrese las horas "))
while horas < 0:
    horas = int(input("ingrese horas correctas "))
if horas > 5:
    print (f"debe pagar {(hora * horas)+ multa}")
else:
    print (f"debe pagar {hora * horas}")'''

#7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

#Menú: $12.000

#Opciones bebida:

#    sí → $3.000
#    no → $0

#Luego aplicar IVA del 8% al total final.
#Mostrar valor con IVA incluido.

'''menu = 12000
bebida= 3000
iva= 0.08
menu2= menu + bebida
print("EL menu cuesta $12.000 más IVA")
pedido=str(input("desea incluir bebida, si o no "))
while pedido != "si" and pedido != "no":
    pedido=str(input("digite si o no "))
if pedido == "si":
    print(f"El costo de menu y la bebida es de : {(menu2)+(menu2 * iva)}")
else:
    print(f"El costo del menu es:{(menu) +(menu * iva) } ")'''

#8. Empresa “TecnoPlus” — Evaluación compuesta

#El usuario ingresa dos notas (0.0 - 5.0):

#    Prueba técnica (70%)
#    Prueba lógica (30%)

#Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

#Condiciones:

#    nota_final ≥ 3 → “Aprobado”
#    2 ≤ nota_final < 3 → “Revisión”
#    < 2 → “Reprobado”

#Validar que las notas estén en rango.

'''tecnica=float(input("Ingrese la nota de la prueba técnica "))
while tecnica < 0.0 or tecnica > 5.0:
    tecnica=float(input("Ingrese una nota valida "))

logica=float(input("Ingrese la nota de la prueba lógica "))
while logica < 0.0 or logica > 5.0:
    logica=float(input("Ingrese una nota valida "))
notafinal= (tecnica * 0.7) + (logica * 0.3)
if notafinal >= 3:
    print(f"su nota final es: {notafinal} y usted fue Aprobado")
elif notafinal  >= 2 and notafinal < 3:
    print(f"su nota final es: {notafinal} y usted esta en Revisión ")
else:
    print(f"su nota final es: {notafinal} y usted esta en Reprobado ")'''

#9. Supermercado “AhorroMax” — Descuentos y envío

#Cada producto cuesta $2.000.

#Reglas:

#        30 unidades → 15% descuento

#        10 unidades → 5% descuento

#    Si el total después del descuento es < $50.000 → agregar $5.000 de envío

#Calcular total final.

'''producto = 2000

precio= int(input("Ingrese el numero total de productos"))
while precio < 0:
    precio=int(input("ingrese una cantidad positiva"))
if precio >= 30:
    total= producto * precio
    if total < 50000:
        print(f"su pago total es: {(total * 0.85) + 5000}")
    else:
        print(f"su pago total es: {total * 0.85}")
elif precio >= 10 and precio <= 29:
    total= producto * precio
    if total < 50000:
        print(f"su pago total es: {(total * 0.95) + 5000}")
    else:
        print(f"su pago total es: {total * 0.95}")
else:
    total= producto * precio
    if  total < 50000:
        print(f"su pago total es: {(total) + 5000}")
    else:
        print(f"su pago total es: {total}")'''

#10. Club “Noche Estelar” — Acceso + validación documento

#Pedir edad y documento.

#Reglas:

#   Edad ≥ 18 → puede entrar solo si tiene documento.
#   Si la edad < 18 → "Entrada denegada"
#    Si tiene 18 o más pero no tiene documento → "Debe presentar documento"

edad= int(input("Ingrese su edad"))
while edad < 0:
    edad=int(input("presente una edad correcta"))
if edad <= 17:
    print("Entrada denegada")
else:
    documento= str(input("tiene documento si o no"))
    if documento == "si":
        print("puede entrar")
    else:
        print("debe presentar documento")






    


