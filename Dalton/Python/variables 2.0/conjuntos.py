#creando un conjunto con set
conjunto = set(["Dato 1","Dato 2"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1,"dato 3"}


print(conjunto2)

#Teoiria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)
resultado = conjunto2 <= conjunto1

#Verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#Verificar si hay algun numero en comun, si no los tiene es True
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)