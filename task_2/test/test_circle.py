import math

import pytest

from task_2.figures.circle import Circle
from task_2.figures.virtual import Figure


@pytest.fixture
def circle():
    """Фикстура для создания экземпляра Circle."""
    return Circle(5.0)


def test_circle_is_instance_of_figure(circle):
    """Проверяет, что Circle является наследником Figure."""
    assert isinstance(circle, Figure)


def test_circle_initial_radius(circle):
    """Проверяет корректность установки радиуса при инициализации."""
    assert circle.radius == 5.0


def test_circle_radius_setter_positive(circle):
    """Проверяет корректную установку положительного радиуса."""
    circle.radius = 10.0
    assert circle.radius == 10.0


@pytest.mark.parametrize("invalid_radius", [-5.0, 0, -0.1])
def test_circle_radius_setter_negative_or_zero(circle, invalid_radius):
    """Проверяет, что установка отрицательного или нулевого радиуса вызывает ValueError."""
    with pytest.raises(ValueError, match="Радиус должен быть положительным числом"):
        circle.radius = invalid_radius


def test_circle_square_calculation(circle):
    """Проверяет корректность вычисления площади."""
    expected_area = math.pi * 5.0**2
    assert circle.square() == pytest.approx(expected_area, rel=1e-6)


def test_circle_square_after_radius_change(circle):
    """Проверяет пересчет площади после изменения радиуса."""
    circle.radius = 3.0
    expected_area = math.pi * 3.0**2
    assert circle.square() == pytest.approx(expected_area, rel=1e-6)


def test_circle_repr_method(circle):
    """Проверяет строковое представление объекта."""
    assert repr(circle) == "Circle(radius=5.0)"


def test_circle_different_radius_values():
    """Проверяет создание кругов с разными радиусами."""
    circle1 = Circle(1.0)
    circle2 = Circle(2.5)
    circle3 = Circle(100.0)

    assert circle1.radius == 1.0
    assert circle2.radius == 2.5
    assert circle3.radius == 100.0
    assert circle1.square() == pytest.approx(math.pi)
    assert circle3.square() == pytest.approx(math.pi * 10000)
