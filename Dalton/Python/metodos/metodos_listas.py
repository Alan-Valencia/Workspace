#Creando una lista con list()
lista = list(["hola","Dalto","34",True,45])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("jajaja")

#agregando un elemento a la lista en un indice especifico
lista.insert(2,"jajaja")

#agregando varios elementos a la lista
lista.extend([True,"jajaja"])

#eliminando un elemento de la lista por su indice
lista.pop(0) #-1 para eliminar el ultimo, -2 para eliminar el anteultimo, y asi sucesivamente.

#removiendo un elemento de la lista por su valor
lista.remove(45)

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (si usaamos el parametro reverse=True la ordena en reversa)
lista.sort()

#invirtiendo los eleemntos de una lista
lista.reverse()


print()