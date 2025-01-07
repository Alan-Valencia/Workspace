import random


print("Juego sencillo pero divertido")
jugador = int(input("Elige: 1 para piedra, 2 para papel, 3 para tijera: "))
pc = random.randint(1,3)

# Jugador
if jugador == 1:
    print("Elegiste piedra")
elif jugador == 2:
    print("Elegiste papel")
elif jugador == 3:
    print("Elegiste tijera")
else:
    print("Invalida")

# PC
if pc == 1:
    print("PC eligio piedra")
elif pc == 2:
    print("PC eligio papel")
elif pc == 3:
    print("PC eligio tijera")


# Combate
if jugador == pc:
    print("Empate")
elif (jugador == 3 and pc == 2) or (jugador == 1 and pc == 3) or (jugador == 2 and pc == 1):
    print("GANASTE")
else:
    print("PERDISTE")