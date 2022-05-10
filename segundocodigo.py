#cuanto fue el total de la cuenta
totalFactura = int(input("por favor ingrese el valor total de la factura:"))

#pedirle a ususario el valos que quiere dar de propina
totalPropina = int(input("por favor ingrese el valor de la propina:"))

total = (totalFactura * totalPropina / 100) + (totalFactura)

print (f"el total a pagar con propina es de {total} pesos")