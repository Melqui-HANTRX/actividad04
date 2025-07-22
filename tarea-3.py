usuarios = ["pedro", "rosa", "enma"]
contras = ["432343", "etc", "epilogo"]

intentosDeusuario = 0
log = False

while intentosDeusuario < 3 and not log:
    usersvalidados = input("Ingrese su Usuario: ")
    contraseña = input("Ingrese la Contraseña: ")
    i = 0
    valido = False
    while i < 3 and not valido:
        if usersvalidados == usuarios[i] and contraseña == contras[i]:
            valido = True
        i += 1
    if valido:
        log = True
    else:
        intentosDeusuario += 1
        print("Usuario o contraseña incorrectos.")
if not log:
    print("ACCESO BLOQUEADO")
else:
    print("Acceso concedido.")
    print("Menú:")
    print("1. Ver perfil")
    print("2. Cambiar contraseña")
    print("3. Cerrar sesión")
