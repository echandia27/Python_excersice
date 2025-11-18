# 2. Gestor de Tareas Diarias

# Descripción:
# Simula una app de tareas pendientes (To-Do List).

# Debe permitir:

#     Agregar tareas.
#     Marcar tareas como completadas.
#     Eliminar tareas.
#     Mostrar todas las tareas (pendientes y completadas).
#     Salir del sistema.

tareas=[]

def agregar_tarea():
    agregar=str(input("Agregue una tarea a la lista\n"))
    tareas.append({"tarea":agregar, "completada":False})
    print("\nTarea agregada")

def marcar_tarea():
    mostrar_tarea()

    try:
        indice=int(input("\nAgregue que tarea acompletado")) -1
        if 0 <=indice < len(tareas):
            tareas[indice]["completada"]=True
            print("\nTarea Completada")
        else:
            print("Numero fuera de los parametos")
    except ValueError:
        print("\nDebe ingresar un numero")

def mostrar_tarea():
    if not tareas:
        print("\nNo hay tareas registradas")
        return
    print("\nLista de Tareas")
    for i, agregar in enumerate(tareas, start=1):
        if agregar["completada"]:
            estado="✔️ completada" 
        else:
            estado="🕒 pendiente"

        print(f"{i}. {agregar['tarea']}- {estado}")

def eliminar_tarea():
    mostrar_tarea()

    try:
        indice=int(input("\nQue tarea desea eliminar?")) -1
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
        else:
            print("\nNumero de tarea invalido")
    except ValueError:
        print("\nDebes ingresar un numero valido")




while True:

    print("\n<==GESTOR DE TAREAS==>")
    print("1. agregar tareas")
    print("2. marcar tareas como completadas")
    print("3. eliminar tareas")
    print("4. mostrar tareas")
    print("5. Salir del sistema")

    try:
        opcion=int(input("Selececiona el número a donde quieres ir\n"))
    except ValueError:
        print("Seleciona un numero dentro de los parametros")
        continue

    if opcion == 1:
        agregar_tarea()

    elif opcion == 2:
        marcar_tarea()

    elif opcion ==3:
        eliminar_tarea()
    
    elif opcion == 4:
        mostrar_tarea()

    elif opcion == 5:
        print("\nSesion terminada")
        break

    else:
        print("\nOpcion Invalida intenta de nuevo")