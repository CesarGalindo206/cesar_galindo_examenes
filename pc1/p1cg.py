#Parte 1

#Variables

nombre1 = "Cesar"
apellido1 = "Galindo"
salario =  1234
edad = "20"
compañia = "Black Mesa Research Facility"


print("El tipo de variable del nombre es ", type(nombre1))
print("El tipo de variable del salario es ", type(salario))
print("El tipo de variable del edad es ", type(edad))
print("El tipo de variable de la compañia es", type(compañia))

print("-----------------------------------------------------")
if int(edad) > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre")
    bono_final = pow(salario, 2) + salario * 0.10
    print("Su bono final es",bono_final)
else:
    print("Usted tiene un bono de 5% en el mes de diciembre")
    bono_final = pow(salario, 2) + salario * 0.05
    print("Su bono final es",bono_final)

# Parte 3







