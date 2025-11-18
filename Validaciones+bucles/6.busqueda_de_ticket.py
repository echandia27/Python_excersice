# 6) Soporte “Búsqueda de ticket” — Encontrar primera coincidencia
# Como agente de soporte, quiero una función buscar_ticket(tickets, codigo) que valide si codigo está y devuelva su índice.

# Si no existe, retorna -1.
# Usa un bucle para confirmar si hay duplicados y contarlos.
# Sugerencia: usa list.index() (maneja excepciones) y/o list.count().

tickets=["a1","a2","a3","a2","a3","a3","a4"]

#esta seria la funcion usando un bucle

def buscar_ticket(tickets, codigo):
    try:
        indice=tickets.index(codigo)
    except ValueError:
        return-1
    
    contador=0

    for i in tickets:
        if i == codigo:
            contador+=1

    print(f"el codigo {codigo} aparece {contador} veces")
    return indice

print(f" desde la posicion {buscar_ticket(tickets, "a3")}")

#ahora usare tanto list.index como list.count

def buscar_ticket2(tickets, codigo):
    try:
        indic=tickets.index(codigo)
    except ValueError:
        return -1
    
    cantidad=tickets.count(codigo)
    print(f"el codigo {codigo} aparece {cantidad} de veces")
    return indic
print(f"desde el posicion {buscar_ticket2(tickets, "a2")}")