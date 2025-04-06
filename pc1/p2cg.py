#Parte 2

#Variables

nombre1 = "Cesar"
apellido1 = "Galindo"
salario =  1234
edad = "20"
compañia = "Black Mesa Research Facility"
bono_final = pow(salario, 2) + salario * 0.05

boolean1 = False

lite = []

lite.append(nombre1)
lite.append(apellido1)
lite.append(salario)
lite.append(edad)
lite.append(compañia)
lite.append(bono_final)
lite.append(boolean1)

print("La lista con la información del usuario es ahora: {} y el tamaño de esta es: {}".format(lite,len(lite)))

if boolean1:
    print("El trabajador {} {} se encuentra trabajando actualmente en la compañia".format(nombre1,apellido1))

else:
    print("El trabajador {} ya no se encuentra trabajando actualmente en la empresa".format(nombre1))

