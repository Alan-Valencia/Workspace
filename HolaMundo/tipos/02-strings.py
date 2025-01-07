# nombre_curso = "Ultimate Python"
# descripcion_curso = """
# Ultimate Python, este curso contempla todos los detalles

# """
# print(len(nombre_curso))
# print(nombre_curso[0])
# print(nombre_curso[0:8])
# print(nombre_curso[9:])
# print(nombre_curso[:])


# nombre = input("Ingresa nombre: ")
# apellido = input("Ingresa apellido: ")

# usuario1 = nombre[:3] + apellido
# usuario2 = nombre[0] + apellido[:5]
# usuario3 = nombre + apellido[:4]

# print(f"Nombres sugeridos: {usuario1}, {usuario2}, {usuario3}")


#Contador de palabras

# from re import split


# oracion = input("Escribe una oración: ")
# palabras = oracion.split()

# print(f"La oración tiene {len(palabras)} palabras.")


#Formato de texto automático

# titulo_libro = input("Escribe el titulo de un libro: ")

# formateado = (titulo_libro.title())  # las primeras letras las pone en mayusculas

# if len(formateado) > 20:
#     formateado = formateado [:17] + "..."

# print(f"Título formateado: {formateado}")


#Extracción de iniciales

nombre_completo = input("Escribe tu nombre completo: ")
partes = nombre_completo.split()

iniciales = "".join([parte[0].upper() for parte in partes])
print(f"Iniciales: {iniciales}")

#Verificador de palíndromos

palabra = input("Introduce una palabra: ").lower().replace(" ", "")
es_palindromo = palabra == palabra[::-1]

if es_palindromo:
    print(f"{palabra} es un palíndromo")
else:
    print(f"{palabra} no es un palíndromo")

#Contador de vocales

oracion = input("Introduce una oración: ").lower()
vocales = "aeiou"
contador = sum(1 for letra in oracion if letra in vocales)

print(f"Hay {contador} vocales en la oración.")