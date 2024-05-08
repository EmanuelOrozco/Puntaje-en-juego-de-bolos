import abc
from abc import ABC
from dataclasses import dataclass

@dataclass
class Roll:
    pins: int

class Frame(ABC):
    def __init__(self):
        self.rolls: list[Roll] = []
        self.next_frame: Frame | None = None

    @abc.abstractmethod
    def add_roll(self, pins: int):
        raise NotImplementedError

    @abc.abstractmethod
    def score(self):
        pass
    def is_spare(self) -> bool:
        return len(self.rolls) == 2 and self.rolls[0].pins + self.rolls[1].pins == 10


    def is_strike(self) -> bool:
        return len(self.rolls) > 0 and self.rolls[0].pins == 10


class NormalFrame(Frame):
    def score(self):
        pass

    def add_roll(self, pins: int):
        pass

    def __init__(self):
        super().__init__()



class TenthFrame(Frame):

    def __init__(self):
        super().__init__()
        self.extra_roll: Roll | None = None
    def score(self):
        pass

    def add_roll(self, pins: int):
        pass


class BowlingGame:
    def __init__(self):
        self.frames: list[Frame] = []
        self.__init_frames()

    def __init_frames(self):
        frame = NormalFrame()
        for i in range(9):
            if i < 8:
                next_frame = NormalFrame()
            else:
                next_frame = TenthFrame()

            frame.next_frame = next_frame
            self.frames.append(frame)
            frame = next_frame

    def roll(self, pins: int):
        pass

    def score(self) -> int:
        pass


