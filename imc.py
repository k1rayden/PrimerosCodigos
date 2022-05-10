#ingresar el peso en KG
pesoPersona = float(input("por favor ingrese su peso en kilogramos: "))
#estatura en metros

estaturaPersona = float(input("por favor ingrese su estaruta en metros"))

#calcular IMC

imc = pesoPersona / (estaturaPersona ** 2)

#imprimir el IMC

if imc <= 18.5:
    print(f"tiene un peso inferior al normal, tu imc es de {imc} kg / m2")
elif imc >=18.5 and imc <= 24.9:
    print(f"tiene un peso normal, tu imc es {imc}")
elif imc >= 25 and imc <= 29.9:
    print (f"tienes un peso superior al normal, tu imc es de {imc} kg/m2")
else: 
    print (f"sufres de obesidad, intenta bajar de peso, tu imc es de {imc}")


