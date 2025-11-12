# 20. Aplicación “Inicio Seguro” – Intentos de inicio de sesión
# Como usuario, quiero usar un while con máximo 3 intentos de contraseña.
# Si acierto, mostrar “Acceso permitido”.
# Si agoto los intentos, mostrar “Acceso denegado”.

contrasecorrecta= "juan"
intentos= 1
while intentos <= 3:
    constraseña=str(input("Ingrese contraseña "))
    if constraseña == contrasecorrecta:
        print("Acceso permitido")
        break
    else:
        print("Acceso denegado")
        intentos += 1

