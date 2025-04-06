#Parte 3

#Variables

nombre1 = "Cesar"
apellido1 = "Galindo"
salario =  1234
edad = "20"
compañia = "Black Mesa Research Facility"
boolean1 = False
bono_final = pow(salario, 2) + salario * 0.05
num_hij = 3

lite = [nombre1,apellido1,salario,edad,compañia,bono_final,boolean1,num_hij]

if num_hij > 1:
    bono_familiar = salario*0.08
    lite.append(bono_familiar)
    print("Obtiene el bono familiar el cual es {}".format(bono_familiar))
    print("Ahora la lista actualizada es {}".format(lite))
else:
    print("No cumple para obtener el bono familiar")