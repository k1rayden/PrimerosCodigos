# paso 1 pedir el total de la factura

totalFactura= int(input("ingrese el valor de la factura:"))

#paso 2 pedir el porcentaje de la propina que se quiere dar

propina= int(input("ingrese el % de propina que quiere dar:"))



#paso 3 calcular el valor del iva del 19%
valorDelIva= totalFactura * 0.19

#paso 4 calcular el subtotal toal de la factura - valor del iva

total= totalFactura - valorDelIva

#paso 5 calcular el valor de la propina subtotal * propina /100

valoPropina = total * propina /100

#paso 6 mostrar el resultado
print(f"el total a pagar es de : {valoPropina} pesos")
print(f"el valor del IVA fie: {valorDelIva} pesos")
print(f"el subtotal fue : {total} pesos")