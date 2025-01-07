squares = [x**2 for x in range(1,10)]
# print("Cuadrados: ", squares)

celcius = (0, 10, 20, 30, 40)
farenheit = [(temp *9/5) + 32 for temp in celcius]
# print("Temperatura en F: ", farenheit)

# Numeros pares
evens = [x for x in range(1,21) if x %2 == 0]
# print(evens)

# Ejercicio1
numeros = [1, 2, 3, 4, 5]
dobles = [num * 2 for num in numeros]
print(numeros)
print(dobles)

# Ejercicio2
palabras = ["sol", "mar", "montaña", "rio", "estrella"]
resultado = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print(resultado)

# ejericio 3
claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]
diccionario = {claves[x] : valores[x] for x in range (len(claves))}
print(diccionario)