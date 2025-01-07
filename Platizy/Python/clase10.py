import random

# Solicitar la elección del jugador
jugador = int(input("Elige: 1 para piedra🤘, 2 para papel📄, 3 para tijera✂️: "))

# PC elige aleatoriamente entre 1, 2, 3
pc = random.randint(1, 3)

# Mostrar la elección del jugador
if jugador == 1:
    print("Elegiste piedra🤘")
elif jugador == 2:
    print("Elegiste papel📄")
elif jugador == 3:
    print("Elegiste tijera✂️")
else:
    print("Elección no válida")

# Mostrar la elección de la computadora
if pc == 1:
    print("PC elige piedra🤘")
elif pc == 2:
    print("PC elige papel📄")
elif pc == 3:
    print("PC elige tijera✂️")

# COMBATE
if pc == jugador:
    print("EMPATE")
elif (jugador == 1 and pc == 3) or (jugador == 2 and pc == 1) or (jugador == 3 and pc == 2):
    print("¡GANASTE!")
else:
    print("PERDISTE")
