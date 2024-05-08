
class Frame:
    def _init_(self):
        self.rolls: list = []

    def roll(self, pins):
        if pins < 0 or pins > 10:
            raise ValueError("Los pines deben estar entre 0 y 10")
        self.rolls.append(pins)

    def score(self):
        return sum(self.rolls)

    def is_strike(self):
        return len(self.rolls) == 1 and self.score() == 10

    def is_spare(self):
        return len(self.rolls) == 2 and self.score() == 10


class Game:
    def _init_(self):
        self.frames = [Frame() for _ in range(10)]
        self.current_frame = 0

    def roll(self, pins):
        if self.current_frame == 10:
            raise ValueError("No puedes lanzar más, el juego ha terminado")
        frame = self.frames[self.current_frame]
        frame.roll(pins)
        if frame.is_strike() or len(frame.rolls) == 2:
            self.current_frame += 1

    def score(self):
        score = 0
        for i in range(10):
            frame = self.frames[i]
            score += frame.score()
            if frame.is_strike():
                score += self.frames[i + 1].score()
                if self.frames[i + 1].is_strike() and i < 8:
                    score += self.frames[i + 2].rolls[0]
            elif frame.is_spare():
                score += self.frames[i + 1].rolls[0]
        return score