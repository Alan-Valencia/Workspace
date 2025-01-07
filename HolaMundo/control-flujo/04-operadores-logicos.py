# and, or, not

gas = True
encendido = True
edad = 18

# if gas or encendido:
#     print("Puedes avanzar")
# else:
#     print("No puedes avanzar")

# if gas and encendido and edad >= 18:
#     print("Puedes avanzar")

# if not gas and (encendido or edad > 17):
#     print("Puedes avanzar")

if not gas or encendido or edad > 17:
    print("Puedes avanzar")
