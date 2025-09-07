import math

from figures.virtual import Figure


class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        if not self.is_valid_triangle(side_a, side_b, side_c):
            raise ValueError("Треугольник с такими сторонами не существует")
        self.a = side_a
        self.b = side_b
        self.c = side_c

    @staticmethod
    def is_valid_triangle(a: float, b: float, c: float) -> bool:
        return a + b > c and a + c > b and b + c > a and a > 0 and b > 0 and c > 0

    @property
    def a(self) -> float:
        return self.__a

    @property
    def b(self) -> float:
        return self.__b

    @property
    def c(self) -> float:
        return self.__c

    @a.setter
    def a(self, a: float) -> None:
        if a <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.__a = a

    @b.setter
    def b(self, b: float) -> None:
        if b <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.__b = b

    @c.setter
    def c(self, c: float) -> None:
        if c <= 0:
            raise ValueError("Сторона должна быть положительной")
        self.__c = c

    def square(self) -> int | float:
        if not self.is_valid_triangle(self.a, self.b, self.c):
            return 0
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def right(self) -> bool:
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)

    def __repr__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"
