
from modulofinal import (aleatorios as al_,
                         almacen_norep as np_, maymeno as mm_, maxlis as maxi)

listaprueba = al_()
print(f"\nLa lista de números aleatorios es {listaprueba}")
print("__________________________________________"
      "__________________________________________"
      "________________________")
listaprueba2 = np_(listaprueba)
print(f"La lista de números no repetidos "
      f"provenientes de la anterior es {listaprueba2}")
print("__________________________________________"
      "__________________________________________"
      "________________________")
listaprueba3 = mm_(listaprueba2)
print(f"La lista de números no repetidos "
      f"ordenada de menor a mayor es {listaprueba3}")
print("__________________________________________"
      "__________________________________________"
      "________________________")
print(f"El mayor número par de la lista "
      f"de números no repetidos es {maxi(listaprueba2)}")
