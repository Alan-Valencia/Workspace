#Creando diccionarios con dict()
diccionario = dict(nombre="lucas",apellido="dalto")

#las listas no pueden ser claves, con tuplas si, con conjunto (frozenset)
diccionario = {("dalto","rancio"):"jaja"}

#creando diccionarios con fromkeys() valor por defecto :none
diccionario = dict.fromkeys(["nombre", "apellido"])

#creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys("ABCDEF","no se")

print(diccionario)