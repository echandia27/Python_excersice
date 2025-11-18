# **8) Academia “Registro ordenado” — Orden asc/desc configurable**  
# *Como coordinador,* quiero una función `ordenar_registros(registros, descendente=False)` que **valide** que todos
# los elementos sean comparables y ordene.  
# - Si `descendente` es `True`, ordenar en orden inverso.  
# - Recorre la lista para imprimir el TOP 3.
'''lista=["holoa", "sadks","dasas", "djaskdj", ]
def ordenar_registro(registro, desendente=False):
    numericos=(int, float)
    boleanos=(bool,)
    string=(str,)
    nuevo=registro[0]
    if isinstance(nuevo, numericos):
        nuevo= numericos
    if isinstance(nuevo, boleanos):
        nuevo= boleanos
    if isinstance(nuevo, string):
        nuevo=string
    try:
        for i in registro:
            if isinstance(i, nuevo):
                if desendente == False:
                    registro.sort()
                
                elif desendente == True:
                    registro.sort(reverse=False)
                else: 
                    print("Debe ser un boleano")    

        for i in registro[0:3]:

            print(i)
    except TypeError as e:
        print(f"Error en la lista, datos no concuerdan. {e}")        

ordenar_registro(lista, False)

def ordenars_registros(registros, descendente=False):
    # Revisar si todos los elementos son comparables
    tipos = tuple(type(x) for x in registros)
    if len(set(tipos)) > 1:
        print("Error: todos los elementos deben ser del mismo tipo para poder ordenar.")
        return
    
    # Ordenar la lista
    registros.sort(reverse=descendente)
    
    # Mostrar TOP 3
    print("TOP 3 registros:")
    for i in registros[:3]:
        print(i)'''
       
lista=[10,20,5,8,15]

def ordenar_registros(lista, decendente=False):
    tipos={type(x) for x in lista}
    if len(tipos) > 1:
        print("Error: la lista no es comparable")
        return []
    lista.sort(reverse=decendente)

    print("TOP 3:")

    for i in range(min(3, len(lista))):
        print(lista[i])
    return lista
    
ordenar_registros(lista)