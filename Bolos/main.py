from testing2 import BowlingGame

def main():
    game = BowlingGame()
    print("Ingrese los resultados de cada tirada (1-10 pines). 'X' para strike, '/' para spare y '-' para tirada vacía.")

    for frame in range(1, 11):
        roll1 = input(f"Tirada 1 del frame {frame}: ").strip()
        if roll1.upper() == 'X':
            game.roll(10)
        else:
            roll1 = int(roll1)
            game.roll(roll1)

            if roll1 < 10:
                roll2 = input(f"Tirada 2 del frame {frame}: ").strip()
                if roll2 == '/':
                    game.roll(BowlingGame.SPARE)  # Usamos el valor especial para el spare
                elif roll2 == '-':
                    game.roll(0)
                else:
                    roll2 = int(roll2)
                    game.roll(roll2)

    print("Puntaje total del juego:", game.score())


if __name__ == "__main__":
    main()
