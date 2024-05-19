def crear_tablero():
    # Crear un tablero vacío representado como una matriz 8x8
    tablero = [['' for _ in range(8)] for _ in range(8)]
    return tablero

def validar_posicion(tablero, fila, columna):
    # Verificar si las coordenadas están dentro del tablero
    if 0 <= fila < 8 and 0 <= columna < 8:
        return True
    return False

def listar_movimientos_caballo(tablero, fila, columna):
    movimientos = [
        (-2, -1), (-2, 1), (2, -1), (2, 1),
        (-1, -2), (-1, 2), (1, -2), (1, 2)
    ]
    movimientos_validos = []

    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]
        if validar_posicion(tablero, nueva_fila, nueva_columna) and tablero[nueva_fila][nueva_columna] == '':
            movimientos_validos.append((nueva_fila, nueva_columna))
    return movimientos_validos

def imprimir_tablero(tablero):
    # Imprimir etiquetas de columnas
    print('   ', end='')
    for col in range(8):
        print(chr(col + ord('a')), end=' ')
    print()

    # Imprimir filas con etiquetas y contenido del tablero
    for i in range(8):
        print(f'{i+1}  ', end='')
        for j in range(8):
            print(tablero[i][j], end=' ')
        print()

def main():
    tablero = crear_tablero()

    # Solicitar cantidad de piezas a insertar
    num_piezas = int(input("Ingrese el número de piezas a insertar: "))

    # Insertar cada pieza en el tablero
    for i in range(num_piezas):
        tipo_pieza = input(f"Ingrese el tipo de pieza {i+1}: ").lower()
        color = input(f"Ingrese el color de la pieza {i+1} (blanco o negro): ").lower()
        posicion = input(f"Ingrese la posición de la pieza {i+1} (ej. a1, e4, f8): ")

        # Obtener coordenadas de la posición ingresada
        columna = ord(posicion[0]) - ord('a')
        fila = int(posicion[1]) - 1

        # Verificar validez de la posición
        if not validar_posicion(tablero, fila, columna):
            print(f"La posición de la pieza {i+1} ingresada no es válida.")
            return

        # Colocar la pieza en el tablero
        tablero[fila][columna] = f'{tipo_pieza}_{color[0]}'

    # Mostrar el tablero con las piezas colocadas
    print("Tablero con las piezas colocadas:")
    imprimir_tablero(tablero)

    # Listar los movimientos válidos del caballo para cada pieza
    print("\nMovimientos válidos del caballo para cada pieza:")
    for i in range(8):
        for j in range(8):
            if tablero[i][j] != '':
                tipo_pieza, color = tablero[i][j].split('_')
                if tipo_pieza == 'caballo':
                    movimientos_caballo = listar_movimientos_caballo(tablero, i, j)
                    print(f"\nPara la pieza en {chr(j + ord('a'))}{i + 1} ({tipo_pieza} {color}):")
                    for movimiento in movimientos_caballo:
                        nueva_fila, nueva_columna = movimiento
                        print(f"Posición: {chr(nueva_columna + ord('a'))}{nueva_fila + 1}")

if __name__ == "__main__":
    main()


