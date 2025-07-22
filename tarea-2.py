ingresos = float(input("Cual es su ingreso anual (Q): "))
dependiente = int(input("Ingresar numero de dependientes: "))

deduccion = dependiente * 1000
ingresos_neto = ingresos - deduccion

if ingresos < 40000 and dependiente > 2:
 impuesto = 0
else:
    if ingresos_neto <= 30000:
     impuestos = ingresos_neto * 0.05
    elif ingresos_neto <= 60000:
     impuestos = ingresos_neto * 0.10
    elif ingresos_neto <= 100000:
     impuestos = ingresos_neto * 0.15
    else:
     impuestos = ingresos_neto * 0.20
if impuestos < 0:
    impuestos = 0
print(f"Impuesto a pagar: Q{impuestos:.2f}")
