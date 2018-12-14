import random


def sacarDados():
    dado1 = random.randrange(1, 11)
    dado2 = random.randrange(1, 11)
    dado3 = random.randrange(1, 11)
    return [dado1, dado2, dado3]


print("JUEGO DEL QUINCE")
Gloria = sacarDados()
Hector = sacarDados()

print(Gloria)
print(Hector)

print("Carmen ha sacado un " + str(Gloria[0]) + ", " + str(Gloria[1]) + " y " + str(Gloria[2]))
print("David  ha sacado un " + str(Hector[0]) + ", " + str(Hector[1]) + " y " + str(Gloria[2]))


if Gloria[0] + Gloria[1] + Gloria[2] > Hector[0] + Hector[1] + Hector[2] | Gloria[0] + Gloria[1] + Gloria[2] < 15:
    print("Ha ganado Carmen")

elif Gloria[0] + Gloria[1] + Gloria[2] > Hector[0] + Hector[1] + Hector[2] | Hector[0] + Hector[1] + Hector[2] < 15:
    print("Ha ganado David")

else:
    print("han perdido los dos")
