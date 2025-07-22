print("Opciones: sur,norte, oeste, este")
origen = input("Donde se encuentra la persona? ").lower()
destinofinal = input("Hacia donde desea drigirse? ").lower()

direccion = ""

if origen == destinofinal:
    direccion = f"Ya esta en el {origen}"
else:
    if origen in ["norte", "sur"]:
        if destinofinal == "este":
            direccion = "noreste" if origen == "norte" else "sureste"
        elif destinofinal == "oeste":
            direccion = "noroeste" if origen == "norte" else "suroeste"
        else:
            direccion = f"recto hacia el {destinofinal}"
    elif origen in ["este", "oeste"]:
        if destinofinal == "norte":
            direccion = "noreste" if origen == "este" else "noroeste"
        elif destinofinal == "sur":
            direccion = "sureste" if origen == "este" else "suroeste"
        else:
            direccion = f"recto hacia el {destinofinal}"
    else:
        direccion = "Esta direccion es invalida"

print(f"Favor de dirigirse hacia: {direccion}")
