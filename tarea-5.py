print("Bienvenido, al ingresar los datos, deben ser en numeros, gracias")
inDa = int(input("Ingrese el día: "))
inMs = int(input("Ingrese el mes: "))
inÑo = int(input("Ingrese el año: "))

valido = True

if inMs in [1,3,5,7,8,10,12]:
    if inDa < 1 or inDa > 31:
        valido = False
elif inMs in [4,6,9,11]:
    if inDa < 1 or inDa > 30:
        valido = False
elif inMs == 2:
    bisiesto = (inÑo % 400 == 0) or (inÑo % 4 == 0 and inÑo % 100 != 0)
    if bisiesto:
        if inDa < 1 or inDa > 29:
            valido = False
    else:
        if inDa < 1 or inDa > 28:
            valido = False
else:
    valido = False

if not valido:
    print("Fecha inválida, no se encontro en el rango establecido.")
else:
    M = inMs
    Y = inÑo
    if M < 3:
        M += 12
        Y -= 1

    K = Y % 100
    J = Y // 100

    H = (inDa + (13*(M+1))//5 + K + (K//4) + (J//4) + 5*J) % 7

    diasemana = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
    print(f"La fecha {inDa:02d}/{inMs:02d}/{inÑo} fue un {diasemana[H]}")
