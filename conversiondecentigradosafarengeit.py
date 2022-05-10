# ingresar la temperatura en fahrenheit

temperaturaFahrenheit = int(input("por favor ingrese la temperatura en °F"))

# conversion

conversionFaC = (temperaturaFahrenheit - 32) * (5/9)

# mostar la conversion

print(f"la temperatura en grados centigrados es de {conversionFaC} °C")