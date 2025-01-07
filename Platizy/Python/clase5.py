from multiprocessing import Value
from optparse import Values
from typing import Type


numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers[2])
information = {"nombre":"Alan",
               "apellido":"Valencia",
               "altura":1.80,
               "Edad":27}
del information["Edad"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values =information.values()
print(values)
pairs = information.items()
print(pairs)