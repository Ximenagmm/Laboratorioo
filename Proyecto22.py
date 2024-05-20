def crear_tablero():
    
    tablero = [['' for _ in range(8)] for _ in range(8)]
    return tablero

def validar_posicion(tablero, fila, columna):
   
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
   
    print('   ', end='')
    for col in range(8):
        print(chr(col + ord('a')), end=' ')
    print()

   
    for i in range(8):
        print(f'{i+1}  ', end='')
        for j in range(8):
            print(tablero[i][j] if tablero[i][j] != '' else '.', end=' ')
        print()

def main():
    tablero = crear_tablero()

    
    while True:
        try:
            num_piezas = int(input("Ingrese el número de piezas a insertar: "))
            if num_piezas < 0:
                raise ValueError("El número de piezas no puede ser negativo.")
            break
        except ValueError as e:
            print(e)
            continue

    
    for i in range(num_piezas):
        while True:
            try:
                tipo_pieza = input(f"Ingrese el tipo de pieza {i+1}: ").lower()
                if tipo_pieza not in ['peon', 'torre', 'caballo', 'alfil', 'reina', 'rey']:
                    raise ValueError("Tipo de pieza no válido.")
                
                color = input(f"Ingrese el color de la pieza {i+1} (blanco o negro): ").lower()
                if color not in ['blanco', 'negro']:
                    raise ValueError("Color no válido.")
                
                posicion = input(f"Ingrese la posición de la pieza {i+1} (ej. a1, e4, f8): ")
                columna = ord(posicion[0]) - ord('a')
                fila = int(posicion[1]) - 1

                if not validar_posicion(tablero, fila, columna):
                    raise ValueError("La posición ingresada no es válida.")
                if tablero[fila][columna] != '':
                    raise ValueError("Ya hay una pieza en esa posición.")

                
                tablero[fila][columna] = f'{tipo_pieza[0].upper()}_{color[0]}'
                break
            except (ValueError, IndexError) as e:
                print(e)
                continue

    
    print("Tablero con las piezas colocadas:")
    imprimir_tablero(tablero)

    
    print("\nMovimientos válidos del caballo para cada pieza:")
    for i in range(8):
        for j in range(8):
            if tablero[i][j] != '':
                tipo_pieza, color = tablero[i][j].split('_')
                if tipo_pieza == 'C':
                    movimientos_caballo = listar_movimientos_caballo(tablero, i, j)
                    print(f"\nPara la pieza en {chr(j + ord('a'))}{i + 1} ({tipo_pieza} {color}):")
                    for movimiento in movimientos_caballo:
                        nueva_fila, nueva_columna = movimiento
                        print(f"Posición: {chr(nueva_columna + ord('a'))}{nueva_fila + 1}")

if __name__ == "__main__":
    main()

