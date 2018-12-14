import random


def sacarDados():
    dado1 = random.randrange(1, 7)
    dado2 = random.randrange(1, 7)
    total = dado1 + dado2
    return str(dado1) + str(dado2)


def compararMayor(num1j1, num2j1, num1j2, num2j2):
    total = 4
    mayorA = 0
    mayorB = 0
    salida = ""

    if num1j1 > mayorA:
        mayorA = num1j1
        salida = "Carmen"
    if num2j1 > mayorA:
        mayorA = num2j1
        salida = "Carmen"
    if num1j2 > mayorB:
        mayorB = num2j1
        salida = "David"
    if num2j2 > mayorB:
        mayorB = num2j2
        salida = "David"
    print(salida)
    if mayorA == mayorB:
        salida = "igual"

    if salida == "igual":
        print("han empatado")
    else:
        print("Ha ganado " + salida)


print("JUEGO DE DADOS (2)")
Carmen = str(sacarDados())
David = str(sacarDados())

print("Carmen ha sacado un " + Carmen[0:-1] + " y " + Carmen[1:])
print("David ha sacado un " + David[0:-1] + " y " + David[1:])

if int(Carmen[:1]) + int(Carmen[1:]) > int(David[:1]) + int(David[1:]):
    print("Ha ganado Carmen")

if int(Carmen[:1]) + int(Carmen[1:]) < int(David[:1]) + int(David[1:]):
    print("Ha ganado David")

if int(Carmen[:1]) + int(Carmen[1:]) == int(David[:1]) + int(David[1:]):
    compararMayor(int(Carmen[:1]), int(Carmen[1:]), int(David[:1]), int(David[1:]))
