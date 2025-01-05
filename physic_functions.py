import numpy as np
from numpy import ndarray
from abc import ABC, abstractmethod


class FunctionGenerator(ABC):
    @abstractmethod
    def generate_y(self, x: ndarray[np.floating], t: int, *args) -> ndarray[np.floating]:
        pass

    @staticmethod
    @abstractmethod
    def get_formula():
        pass


class StandingWaveFixedBothEndsGenerator(FunctionGenerator):

    def generate_y(self, x: ndarray[np.floating], t: int, a: int, n: float, l: float, v: float) -> ndarray[np.floating]:
        """
        Calculate the value of A*sin(Bx)*cos(wt) for a standing wave.
        :param x: array with current x values
        :param t: current time
        :param a: amplitude
        :param n: harmonic number
        :param l: length of string
        :param v: speed of wave
        :return: y values at given x and time
        """
        k = n * np.pi / l
        omega = v * k
        return a * np.sin(k * x) * np.cos(omega * t)

    @staticmethod
    def get_formula():
        return "A*sin(kx)*cos(ωt)"


class StandingWaveFixedOneEndGenerator(FunctionGenerator):

    def generate_y(self, x: ndarray[np.floating], t: int, a: int, n: int, l: float, v: float) -> ndarray[np.floating]:
        """
        Calculate the value of A*sin((2n-1)*πx/(2l))*cos(wt) for a standing wave fixed at one end.
        """
        k = (2 * n - 1) * np.pi / (2 * l)
        omega = v * k
        return a * np.sin(k * x) * np.cos(omega * t)

    @staticmethod
    def get_formula():
        return "A*sin(((2n+1)πx)/(2L))*cos(ωt)"


class StandingWaveNotFixedGenerator(FunctionGenerator):

    def generate_y(self, x: ndarray[np.floating], t: int, a: int, n: int, l: float, v: float) -> ndarray[np.floating]:
        """
        Calculate the value of A*[sin(kx) + cos(kx)]*cos(wt) for a standing wave not fixed.
        """
        k = n * np.pi / l
        omega = v * k
        return a * (np.sin(k * x) + np.cos(k * x)) * np.cos(omega * t)

    @staticmethod
    def get_formula():
        return "A*[sin(kx) + cos(kx)]*cos(ωt)"


# TODO update generator map after adding new generator
GENERATOR_MAP = {
    "standing_wave_fixed_both_ends": StandingWaveFixedBothEndsGenerator,
    "standing_wave_fixed_one_end": StandingWaveFixedOneEndGenerator,
    "standing_wave_not_fixed": StandingWaveNotFixedGenerator
}
