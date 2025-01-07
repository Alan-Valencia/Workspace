diccionario = {
  "nombre" : "lucas",
  "apellido" : "Dalto",
  "subs" : 1000000
}

#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get( ) (Si no encuentra nada el programa continua)
valor_de_jaja = diccionario.get("jaja")

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("apellido")

#opteniendo un ekemento dict_items iterable
diccionario_iterable = diccionario.items()

print(claves)