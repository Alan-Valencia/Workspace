# El for sirve principalmente para iterar lista de elementos
buscar = 10
for numero in range(5):  # iterable
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numero buscado")

for char in "ultimate python":
    print(char)
 