import math

import pytest

from task_2.figures.triangle import Triangle


def test_valid_triangle_creation():
    """Тест создания валидного треугольника"""
    triangle = Triangle(3, 4, 5)
    assert triangle.a == 3
    assert triangle.b == 4
    assert triangle.c == 5


def test_triangle_side_setters():
    """Тест сеттеров сторон треугольника"""
    triangle = Triangle(2, 3, 4)
    triangle.a = 5
    triangle.b = 6
    triangle.c = 7
    assert triangle.a == 5
    assert triangle.b == 6
    assert triangle.c == 7


def test_invalid_side_setter_raises_error():
    """Тест, что сеттер выбрасывает ошибку для неположительных значений"""
    triangle = Triangle(2, 3, 4)
    with pytest.raises(ValueError, match="Сторона должна быть положительной"):
        triangle.a = -1
    with pytest.raises(ValueError, match="Сторона должна быть положительной"):
        triangle.b = 0
    with pytest.raises(ValueError, match="Сторона должна быть положительной"):
        triangle.c = -5.5


def test_triangle_square_calculation():
    """Тест вычисления площади треугольника"""
    # Прямоугольный треугольник
    triangle = Triangle(3, 4, 5)
    expected_area = 6.0
    assert math.isclose(triangle.square(), expected_area)

    # Равносторонний треугольник
    triangle = Triangle(5, 5, 5)
    expected_area = 10.825317547305483
    assert math.isclose(triangle.square(), expected_area)

    # Произвольный треугольник
    triangle = Triangle(7, 8, 9)
    expected_area = 26.832815729997478
    assert math.isclose(triangle.square(), expected_area)


def test_right_triangle_detection():
    """Тест определения прямоугольного треугольника"""
    # Классический прямоугольный треугольник
    triangle = Triangle(3, 4, 5)
    assert triangle.right() is True

    # Другой прямоугольный треугольник
    triangle = Triangle(5, 12, 13)
    assert triangle.right() is True

    # Не прямоугольный треугольник
    triangle = Triangle(2, 3, 4)
    assert triangle.right() is False

    # Еще один не прямоугольный
    triangle = Triangle(5, 5, 5)
    assert triangle.right() is False


def test_right_triangle_with_float_sides():
    """Тест прямоугольного треугольника с float сторонами"""
    # Треугольник с плавающей точкой (почти прямоугольный)
    triangle = Triangle(3.0, 4.0, 5.0)
    assert triangle.right() is True

    # С плавающей точкой, но не прямоугольный
    triangle = Triangle(3.1, 4.0, 5.0)
    assert triangle.right() is False


def test_triangle_repr():
    """Тест строкового представления"""
    triangle = Triangle(3, 4, 5)
    expected_repr = "Triangle(a=3, b=4, c=5)"
    assert repr(triangle) == expected_repr


def test_triangle_properties():
    """Тест свойств (properties) треугольника"""
    triangle = Triangle(6, 8, 10)
    assert triangle.a == 6
    assert triangle.b == 8
    assert triangle.c == 10


def test_multiple_triangle_instances():
    """Тест создания нескольких экземпляров треугольника"""
    triangle1 = Triangle(3, 4, 5)
    triangle2 = Triangle(6, 8, 10)

    assert triangle1.square() == 6.0
    assert math.isclose(triangle2.square(), 24.0)
    assert triangle1.right() is True
    assert triangle2.right() is True


def test_triangle_with_invalid_sides_after_creation():
    """Тест, что нельзя установить невалидные стороны после создания"""
    triangle = Triangle(2, 3, 4)

    # Проверяем, что сеттеры работают корректно
    with pytest.raises(ValueError):
        triangle.a = 0

    with pytest.raises(ValueError):
        triangle.b = -1
