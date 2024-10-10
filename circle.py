import math


def area(r):
    """
    Находит площать круга.

        Параметры:
            r (float): Радиус круга.

        Возвращаемое значение:
            area (float): Площадь круга.
    """
    return math.pi * r * r


def perimeter(r):
    """
    Находит периметр окружности.

        Параметры:
            r (float): Радиус окружности.

        Возвращаемое значение:
            perimeter (float): Периметр окружности.
    """
    return 2 * math.pi * r

print(perimeter(3))