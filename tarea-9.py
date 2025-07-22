edadusuario = int(input("Que edad tiene?: "))
diadelasemana = input("Que dia de la semana es?: ").lower()
estudiante = input("¿Es estudiante? (sí/no): ").lower()

if edadusuario < 13:
    print("Acceso denegado: No puede ver películas mayores de 13.")
else:
    precios = 50
    if estudiante == "sí" or estudiante == "si":
        precios = 35

    if diadelasemana == "miércoles":
        precios = precios / 2
        print(f"Promoción 2x1, Precio por persona: Q{precios:.2f}")
    else:
        print(f"Precio de su entrada: Q{precios:.2f}")