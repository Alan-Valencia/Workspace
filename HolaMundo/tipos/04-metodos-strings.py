animal = "  chanCHito feliz  "
print(animal.upper())  # Pasa todo mayusculas
print(animal.lower())  # Pasa todo a minuscular
print(animal.strip().capitalize()) # Pasa todo a minusculas con excepción de la primer letra que la pasa a mayuscula
print(animal.title())  # las primeras letras las pone en mayusculas
print(animal.strip())  # Quita espacios en general
print(animal.rstrip())  # Quita espacios en la izquierda
print(animal.lstrip())  # Quita espacios en la derecha
print(animal.find("cH"))  # esta te da el indice y -1 es no lo encontre
# Remplaza lo que le indicamos por otro valor
print(animal.replace("nCH", "j"))
print("nCH" in animal)  # Bolean de si se encuentra o no
print("nCH" not in animal)  # Bolean de si se encuentra o no
