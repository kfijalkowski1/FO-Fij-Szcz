import numpy as np
from numpy import ndarray
from abc import ABC, abstractmethod

class FunctionGenerator(ABC):
    @abstractmethod
    def generate_y(self, x: ndarray[tuple[int, ...], np.dtype[np.floating]], t: int, b: int):
        pass


class SinFunctionGenerator(FunctionGenerator):
    A_MIN = 0.5
    A_MAX = 2.5

    def generate_y(self, x: ndarray[tuple[int, ...], np.dtype[np.floating]], t: int, b: int):
        """
        Calculate the value of A*sin(Bx) at a given x and time.
        :param x: table with current x values
        :param t: current time
        :param b: frequency multiplier
        :return:
        """
        a = self.A_MIN + (self.A_MAX - self.A_MIN) * (t / 99)
        return a * np.sin(b * x)

class CosFunctionGenerator(FunctionGenerator):
    A_MIN = 0.5
    A_MAX = 2.5

    def generate_y(self, x: ndarray[tuple[int, ...], np.dtype[np.floating]], t: int, b: int):
        """
        Calculate the value of A*sin(Bx) at a given x and time.
        :param x: table with current x values
        :param t: current time
        :param b: frequency multiplier
        :return:
        """
        a = self.A_MIN + (self.A_MAX - self.A_MIN) * (t / 99)
        return a * np.cos(b * x)


# TODO add different representation of function


# TODO update generator map after adding new generator
GENERATOR_MAP = {
    "sin": SinFunctionGenerator,
    "cos": CosFunctionGenerator
}