def main():
    # Solicitar los nombres de los jugadores
    jugador1 = input("Ingrese el nombre del jugador 1: ")
    jugador2 = input("Ingrese el nombre del jugador 2: ")
    
    # Inicializar marcador
    marcador = {jugador1: 0, jugador2: 0}
    
    # Inicializar juegos y sets
    juegos_jugador1 = 0
    juegos_jugador2 = 0
    sets_jugador1 = 0
    sets_jugador2 = 0
    
    # Inicializar marcador del juego actual
    marcador_juego = {jugador1: 0, jugador2: 0}
    
    # Función para determinar si un jugador gana un punto
    def gana_punto(marcador_juego, jugador):
        if marcador_juego[jugador] == 0:
            marcador_juego[jugador] = 15
        elif marcador_juego[jugador] == 15:
            marcador_juego[jugador] = 30
        elif marcador_juego[jugador] == 30:
            marcador_juego[jugador] = 40
        elif marcador_juego[jugador] == 40:
            if marcador_juego[oponente(jugador)] == 'Adv':
                marcador_juego[oponente(jugador)] = 40
            elif marcador_juego[oponente(jugador)] == 40:
                marcador_juego[jugador] = 'Adv'
            else:
                ganador_juego(jugador)
        elif marcador_juego[jugador] == 'Adv':
            ganador_juego(jugador)
    
    # Función para determinar quién es el oponente
    def oponente(jugador):
        return jugador1 if jugador == jugador2 else jugador2
    
    # Función para determinar el ganador de un juego
    def ganador_juego(jugador):
        nonlocal juegos_jugador1, juegos_jugador2
        if jugador == jugador1:
            juegos_jugador1 += 1
        else:
            juegos_jugador2 += 1
        # Reiniciar marcador del juego
        marcador_juego[jugador1] = 0
        marcador_juego[jugador2] = 0
    
    # Función para determinar si se ha ganado un set
    def ganador_set():
        nonlocal sets_jugador1, sets_jugador2, juegos_jugador1, juegos_jugador2
        if juegos_jugador1 >= 6 and juegos_jugador1 - juegos_jugador2 >= 2:
            sets_jugador1 += 1
            # Reiniciar juegos
            juegos_jugador1 = 0
            juegos_jugador2 = 0
            return True
        elif juegos_jugador2 >= 6 and juegos_jugador2 - juegos_jugador1 >= 2:
            sets_jugador2 += 1
            # Reiniciar juegos
            juegos_jugador1 = 0
            juegos_jugador2 = 0
            return True
        return False
    
    # Función para imprimir el marcador
    def imprimir_marcador():
        print("\nMarcador:")
        print(f"{jugador1}: {sets_jugador1} sets, {juegos_jugador1} juegos, {marcador_juego[jugador1]}")
        print(f"{jugador2}: {sets_jugador2} sets, {juegos_jugador2} juegos, {marcador_juego[jugador2]}")
    
    # Juego principal
    while True:
        try:
            imprimir_marcador()
            
            # Solicitar al usuario quién gana el punto
            while True:
                punto_ganado = input(f"\n¿Quién gana el punto? ({jugador1} o {jugador2}): ")
                if punto_ganado in [jugador1, jugador2]:
                    break
                else:
                    print("Por favor, ingrese un nombre de jugador válido.")
            
            # Determinar quién gana el punto
            gana_punto(marcador_juego, punto_ganado)
            
            # Verificar si se ha ganado un juego
            if ganador_set():
                print(f"\n¡{punto_ganado} ha ganado el set!")
                # Verificar si se ha ganado el partido
                if sets_jugador1 >= 2 or sets_jugador2 >= 2:
                    print(f"\n¡{punto_ganado} ha ganado el partido!")
                    break
            
        except ValueError as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()




