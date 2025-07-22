pesodelproducto = float(input("Ingrese peso del paquete (kg): "))
distanciadp = float(input("Ingrese la distancia (km): "))
urgenteproducto = input("¿Es urgente? (sí/no): ").lower()
tamañodelproducto = input("Ingrese el tamaño del paquete (pequeño/mediano/grande): ").lower()

cd = (pesodelproducto * 5) + (distanciadp * 0.5)

recargo = 0
descuento = 0

if urgenteproducto == "sí" or urgenteproducto == "si":
    recargo += 50
if tamañodelproducto == "grande":
    recargo += 30
if (urgenteproducto != "sí" and urgenteproducto != "si") and pesodelproducto < 5:
    descuento = 20
total = cd + recargo - descuento
print("\n--- Desglose de Envío ---")
print(f"Costo base: Q{cd:.2f}")
print(f"Recargo: Q{recargo:.2f}")
print(f"Descuento: -Q{descuento:.2f}")
print(f"Total a pagar: Q{total:.2f}")
