# Tablero representado como una lista de listas
tablero = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

# Mostrar el tablero
def mostrar_tablero():
    print("\nTablero actual:")
    for fila in tablero:
        print(' | '.join(fila))

# Verificar si hay un ganador
def hay_ganador(simbolo):
    # Revisar filas
    for fila in tablero:
        if fila.count(simbolo) == 3:
            return True
    # Revisar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] == simbolo:
            return True
    # Revisar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == simbolo:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == simbolo:
        return True
    return False

# Convertir número (1-9) a coordenadas fila/columna
def obtener_coordenadas(posicion):
    posicion = int(posicion) - 1
    fila = posicion // 3
    columna = posicion % 3
    return fila, columna

# Inicia el juego
turno = 'X'
jugadas = 0

print("🎮 Bienvenidos al Juego del Gato (Tres en Línea)")
mostrar_tablero()

while jugadas < 9:
    print(f"\nTurno del jugador {turno}")
    posicion = input("Elige una posición del 1 al 9: ")

    if posicion in [str(n) for n in range(1, 10)]:
        fila, columna = obtener_coordenadas(posicion)

        if tablero[fila][columna] not in ['X', 'O']:
            tablero[fila][columna] = turno
            mostrar_tablero()
            jugadas += 1

            if hay_ganador(turno):
                print(f"\n🎉 ¡Jugador {turno} ha ganado!")
                break

            turno = 'O' if turno == 'X' else 'X'
        else:
            print("❗ Esa posición ya está ocupada.")
    else:
        print("❗ Entrada inválida. Ingresa un número del 1 al 9.")

if jugadas == 9 and not hay_ganador('X') and not hay_ganador('O'):
    print("\n🤝 ¡Empate! El tablero está lleno.")