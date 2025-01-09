# creando las listas
frutas = [
    "banana",
    "manzana",
    "ciruela",
    "pera",
    "naranja",
    "granada",
    "durazno"
]
cadenaC = "Hola Dalto"
numeros = [2, 5, 8, 10]

# evitando que se coma una manzana con la setencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voy a comer una {fruta}')

print("------")

# evitando que el blucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'Me voy a comer una {fruta}')
    if fruta == 'pera':
        break

else:
    print("terminado")

# recorrer una cadena de texto
for letra in cadenaC:
    print(letra)

# for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)

