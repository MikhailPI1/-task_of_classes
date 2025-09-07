import math

from figures.virtual import Figure


class Circle(Figure):

    def __init__(self, radius: int | float) -> None:
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.__radius = value

    def square(self) -> int | float:
        return math.pi * self.__radius**2

    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"
