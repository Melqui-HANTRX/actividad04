finaltotal = 0.0
continuar = True

while continuar:
    precio = input("Ingrese precio del producto ('x' para terminar): ")
    if precio == "x":
        continuar = False
    else:
        i = 0
        valido = True
        while i < len(precio):
            if precio[i] not in "0123456789.":
                valido = False
                i = len(precio)
            else:
                i += 1
        if valido and precio != ".":
            finaltotal += float(precio)
        else:
            print("Precio invalido, por favor intente de nuevo.")

propinas = 0.0
respuesta = input("¿Se le apetece dejar propina? (sí/no): ").lower()
if respuesta == "sí" or respuesta == "si":
    propinas = float(input("¿Cuánto de %? desea dejar: ")) / 100

tarjeta = input("¿Cuenta con tarjeta de cliente frecuente? (sí/no): ").lower()
descuentos = 0.10 if tarjeta == "sí" or tarjeta == "si" else 0.0

iva = finaltotal * 0.12
descuento = finaltotal * descuentos
propina = finaltotal * propinas
total = finaltotal + iva + propina - descuento

print("\n----- Factura -----")
print(f"Subtotal: Q{finaltotal:.2f}")
print(f"IVA (12%): Q{iva:.2f}")
print(f"Propina ({propinas*100:.0f}%): Q{propina:.2f}")
print(f"Descuento ({descuentos*100:.0f}%): -Q{descuento:.2f}")
print(f"Total a pagar: Q{total:.2f}")
