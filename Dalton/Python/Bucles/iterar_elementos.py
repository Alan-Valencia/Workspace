animales = ["perro", "gato", "loro", "cocodrilo"]  # tuplas
numeros = (10, 62, 30, 34)  # listas
numeros = {10, 62, 30, 34}  # listas

# #recorriendo la lista animales
# for animal in animales:
#     print(f"Ahora la variable animal es igual a: {animal}")

# #recorriendo la lista numeros y multiplicando cada valor por 10
# for numero in numeros:
#     resultado = numero * 10
#     print(resultado)


# iterando dos lista del mismo tamaño del mismo tiempo
for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

# forma no optima de recorrer una lista/tupla/conjunto
# for num in range(len(numeros)):
#     print(numeros[num])


# forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"indice es igual a: {indice} y el valor es: {valor}")

# Desempaquetar la tupla directamente
for num, i in enumerate(numeros):
    print(f"indice es igual a: {num} y el valor es: {i}")


# usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
# else:
#     print("El bucle termino")
