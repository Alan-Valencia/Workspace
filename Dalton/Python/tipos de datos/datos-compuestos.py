# creando una lista (Se puede modificar)
lista = [
    "Lucas Dalto",
    "Soy Dalto",
    True,
    1.85
    ]

# creando una tupla (No se puede modificar)
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.80)

# esto es válido
lista[3] = "Maquinola"

# esto no
# tupla[3] = "Maquinola"

# creando un cojunto (set) (no accede a elementos por indice, no almacena datos duplicados)
conjunto = {"Lucas Dalto", "Soy Dalto", True, 1.80}

#print(conjunto[3]) no puede acceder al elemento

#creando diccionarios (dict) (la estructura es key : value y separamos con comas)
diccionario= {
    "nombre" : "Lucas Dalto",
    "canal" : "Soy Dalto",
    "esta_emocionado" : "True",
    "alturaa" : 1.84,
    "dato_duplicado" : "Soy Dalto"
}

print(diccionario["nombre"])