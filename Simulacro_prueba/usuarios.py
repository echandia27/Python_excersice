import csv

def cargar_usuarios():
    usuarios=[]
    try:
        with open ("usuarios.csv", mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                usuarios.append(fila)
        return usuarios
    except FileNotFoundError:
        print("\nNo se encontro el archivo usuarios.csv")
        return []

 #valida que los datos ingresados sean igual a los pedidos   
def validar_credenciales(usuario, contrasena, lista_usuarios):
    for u in lista_usuarios:
        if u["usuario"]== usuario and u["contrasena"]== contrasena:
            return True
    return False

def iniciar_sesion():
    usuarios = cargar_usuarios()
    intentos = 3

    while intentos > 0:
        print("\n----INICIO DE SESION----")
        user=input("Usuario: ")
        pwd=input("Contraseña: ")

        if validar_credenciales(user, pwd, usuarios):
            print("\nInicio de sesion exitoso, Bienvenido a TechLab Inventory Console !")
            return True
        
        intentos -= 1
        print(f"Credencial incorrecta, intentos restantes {intentos}")
    print("\nDemasiados intentos fallidos, el programa se cerrara")
    return False
