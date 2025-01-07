punto =  {"x": 25, "y": 50}

# nombre_variable = {"Llave en string": valor}
print(punto)

# Para ver lo que hay dentro se debe poner dentro de los corchetes el string
print(punto["x"])
print(punto["y"])

punto["z"] = 45
# print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala", punto["lala"])
    
print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25


# Para acceder a los diccionarios se puede hacer de las siguientes formas
for valor in punto:
    print(valor, punto[valor])
    
for valor in punto.items():
    print(valor)

for llave,valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"}
]

for usuario in usuarios:
    print(usuario["nombre"])