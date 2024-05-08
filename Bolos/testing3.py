class Bolos:
    def __init__(self):  # Corrected constructor method
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        roll_index = 0

        for frame in range(10):
            if roll_index < len(self.rolls):  # Verificar que hay lanzamientos suficientes
                if self.is_strike(roll_index):
                    total_score += 10 + self.strike_bonus(roll_index)
                    roll_index += 1
                    # Permitir dos lanzamientos adicionales después de un strike
                    if frame < 9:  # No es el último frame
                        total_score += self.strike_bonus(roll_index)
                        roll_index += 1
                        total_score += self.strike_bonus(roll_index)
                        roll_index += 1
                elif self.is_spare(roll_index):
                    total_score += 10 + self.spare_bonus(roll_index)
                    roll_index += 2
                else:
                    total_score += self.frame_score(roll_index)
                    roll_index += 2
            else:
                break  # Salir del bucle si no hay lanzamientos suficientes

        return total_score

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10 if roll_index < len(self.rolls) else False

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10 if roll_index + 1 < len(self.rolls) else False

    def strike_bonus(self, roll_index):
        if roll_index + 1 < len(self.rolls):
            return self.rolls[roll_index + 1]  # Primer lanzamiento adicional
        else:
            return 0

    def spare_bonus(self, roll_index):
        return self.rolls[roll_index + 2] if roll_index + 2 < len(self.rolls) else 0

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] if roll_index + 1 < len(self.rolls) else 0


# Crear un objeto Bolos
bolos_game = Bolos()

# Solicitar al usuario que ingrese los puntajes de los lanzamientos
for frame in range(10):
    print("Frame", frame + 1)
    roll1 = input("Puntaje del primer lanzamiento ('X' para strike): ")
    if roll1.upper() == 'X':
        bolos_game.roll(10)
        continue
    else:
        roll1 = int(roll1)
    bolos_game.roll(roll1)

    if roll1 < 10:  # Permitir un segundo lanzamiento solo si no es un strike
        roll2 = input("Puntaje del segundo lanzamiento ('/' para spare): ")
        if roll2 == '/':
            bolos_game.roll(10 - roll1)
        else:
            bolos_game.roll(int(roll2))

# Calcular y mostrar el puntaje total
print("Puntaje total:", bolos_game.score())