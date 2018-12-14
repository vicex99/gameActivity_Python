import random


def eleccion():
    item = random.choice(["PIEDRA", "PAPEL", "TIJERA", "LAGARTO", "SPOCK"])
    return item


print("PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK")
ines = eleccion()
juan = eleccion()
ganador = "ines"

print("Ines ha sacado " + ines)
print("juan ha sacado " + juan)

if juan == "PAPEL" and (ines == "PIEDRA" or ines == "LAGARTO"):
    ganador = "juan"
elif juan == "TIJERA" and (ines == "PAPEL" or ines == "SPOCK"):
    ganador = "juan"
elif juan == "PIEDRA" and (ines == "TIJERA" or ines == "SPOCK"):
    ganador = "juan"
elif juan == "SPOCK" and (ines == "PAPEL" or ines == "LAGARTO"):
    ganador = "juan"
elif juan == "LAGARTO" and (ines == "PIEDRA" or ines == "TIJERA"):
    ganador = "juan"
elif ines == juan:
    ganador = "ninguno"

if ganador != "ninguno":
    print("ha ganado " + ganador)
else:
    print("han empatado")