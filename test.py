tablero = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

print("***Tablero Inicial***")
for f in tablero:
        print(" ".join(f))
print()

jugador = "X"
jugadas = 0

while jugadas < 9:
    print("Turno del jugador:", jugador)
    fila = int(input("Ingrese numero de fila (1-3): ")) -1
    columna = int(input("Ingrese numero de columna (1-3): ")) -1

    tablero[fila][columna] = jugador
    jugadas += 1

    for f in tablero:
        print(" ".join(f))
    print()

    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

print("Juego terminado!")
    

