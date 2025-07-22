nombre = input("Nombre completo (al menos 5 letras): ")
if len(nombre) >= 5:
    dpi = input("DPI (debe tener 13 dígitos): ")
    if len(dpi) == 13:
        i = 0
        valido = True
        while i < 13:
            if dpi[i] not in "0123456789":
                valido = False
                break
            i += 1
        if valido:
            departamento = input("Ingrese su Departamento ")
            año = input("Año nacimiento (debe contener 4 dígitos): ")
            if len(año) == 4:
                j = 0
                valido_año = True
                while j < 4:
                    if año[j] not in "0123456789":
                        valido_año = False
                        break
                    j += 1
                if valido_año:
                    edad = 2025 - int(año)
                    if (departamento == "Petén" or departamento == "Alta Verapaz") and edad >= 17 or edad >= 18:
                        print(f"Bienvenido {nombre}, su centro de votación está en {departamento}.")
                    else:
                        print("No cumple con la edad para votar.")
                else:
                    print("Año invalido.")
            else:
                print("Año invalido.")
        else:
            print("DPI invalido.")
    else:
        print("el DPI no puede tener más ni menos de 13 dígitos.")
else:
    print("Nombre invalido(el Nombre debe contener 5 letras por obligacion).")
