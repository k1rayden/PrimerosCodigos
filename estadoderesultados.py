# Pedirle al usuario los ingresos

ingresoIngresos = float(input("por favor ingrese los ingresos: "))

#pedirle al usuario los costos

ingresoCostos = float(input("por favor ingrese los costos :"))


#calcular la utilidad bruta ingresos - costos

utilidadBruta = ingresoIngresos - ingresoCostos

print(f"la utilidad bruta de la empresa es de: {utilidadBruta}")

#pedirle al usuario los gastos

gastos = float(input("por favor ingrese los gastos"))


#calcular la utilidad operativa utilidad bruta - gastos

utilidadOperativa = utilidadBruta - gastos

print(f"la utilidad operativa es de: {utilidadOperativa}")


#calcular el impuesto a la renta utilidad operativa * 30%

impuestoRenta = utilidadOperativa * 30 /100

print(f"el impuesto de renta de la empresa es de {impuestoRenta}")
#calcular utilidad neta utilidad bruta - impuesto a la renta

utilidadNeta = utilidadBruta - impuestoRenta

print(f"la utilidad neta de la empresa es de {utilidadNeta}")

