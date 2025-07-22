estudiantes = []
menor = True

for i in range(5):
    nombre = input(f"Cual es el nombre del estudiante a ingresar {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingrese la nota correspondiente {j+1} de {nombre}: "))
        notas.append(nota)
    promedio = sum(notas) / 3
    if promedio >= 70:
        menor = False
    estudiantes.append([nombre, notas])

if menor:
    for estudiante in estudiantes:
        for i in range(3):
            estudiante[1][i] = min(estudiante[1][i] + 5, 100)
            
print("\nNombre\t\tPromedio")
print("-" * 25)
for est in estudiantes:
    promedio = sum(est[1]) / 3
    print(f"{est[0]:<15} {promedio:.2f}")
