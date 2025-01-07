cadena1 = "Hola soy Dalto"
cadena2 = "Bienvenido maquinola"

#Convierte a mayusculas
resultado = cadena1.upper()

#Convierte a minusculas
resultado = cadena1.lower()

#Primer letra a mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1
busqueda_index = cadena1.index("")

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve lanza una excepcion
busqueda_index = cadena1.index("")

#Si es numerico devuelve True, sino devulve false
es_numerico = cadena1.isnumeric()

#Si es alfanumerico devuelve True, sino devulve false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias 
contar_coincidencia = cadena1.count("")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith()

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith()

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
cadena_nueva = cadena1.replace(","," ")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(contar_coincidencia)