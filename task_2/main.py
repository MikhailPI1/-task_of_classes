from figures.circle import Circle
from figures.triangle import Triangle


circle = Circle(5)
print(f"Площадь круга: {circle.square()}")

triangle = Triangle(3, 4, 5)
print(f"Площадь треугольника: {triangle.square()}")
print(f"Прямоугольный: {triangle.right()}")
