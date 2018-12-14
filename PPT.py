import random


def eleccion():
    item = random.choice(["PIEDRA", "PAPEL", "TIJERA"])
    return item


print("PIEDRA, PAPEL, ... TIJERA!!")
ines = eleccion()
juan = eleccion()
ganador = "ines"

print("Ines ha sacado " + ines)
print("juan ha sacado " + juan)

if ines == "PIEDRA" and juan == "PAPEL":
    ganador = "juan"
elif ines == "PAPEL" and juan == "TIJERA":
    ganador = "juan"
elif ines == "TIJERA" and juan == "PIEDRA":
    ganador = "juan"
elif ines == juan:
    ganador = "ninguno"

if ganador != "ninguno":
    print("ha ganado " + ganador)
else:
    print("han empatado")