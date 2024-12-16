import numpy as np
from numpy import ndarray
from abc import ABC, abstractmethod


class FunctionGenerator(ABC):
    @abstractmethod
    def generate_y(self, x: ndarray[tuple[int, ...], np.dtype[np.floating]], t: int, b: int):
        pass

    @staticmethod
    @abstractmethod
    def get_formula(): pass

    @abstractmethod
    def get_length(self): pass


class StandingWaveFixedBothEndsGenerator:
    A_MIN = 0.5
    A_MAX = 2.5
    LENGTH = 2 * np.pi

    def generate_y(self, x: ndarray[np.floating], t: int, b: int) -> ndarray[np.floating]:
        """
        Calculate the value of A*sin(Bx)*cos(wt) for a standing wave.
        :param x: array with current x values
        :param t: current time
        :param b: frequency multiplier
        :return: y values at given x and time
        """
        a = self.A_MIN# + (self.A_MAX - self.A_MIN) * (t / 99)

        k = (b * np.pi) / self.LENGTH

        omega = 2 * np.pi * b

        y = a * np.sin(k * x) * np.cos(omega * t)
        return y

    @staticmethod
    def get_formula():
        return "A*sin({k:.2f}x)*cos({omega:.2f}t)"

    def get_length(self):
        return self.LENGTH


# TODO add different representation of function


# TODO update generator map after adding new generator
GENERATOR_MAP = {
    "standing_wave_fixed_both_ends": StandingWaveFixedBothEndsGenerator
}
