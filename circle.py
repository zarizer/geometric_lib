import math
import unittest

def area(r):
    """
    Находит площать круга и округляет по четвёртому знаку, чтобы избежать проблем с неточностью float.

        Параметры:
            r (float): Радиус круга.

        Возвращаемое значение:
            area (float): Площадь круга.
    """
    return round(math.pi * r * r, 4)


def perimeter(r):
    """
    Находит периметр окружности и округляет по четвёртому знаку, чтобы избежать проблем с неточностью float.

        Параметры:
            r (float): Радиус окружности.

        Возвращаемое значение:
            perimeter (float): Периметр окружности.
    """
    return round(2 * math.pi * r, 4)

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_int(self):
        res = area(10)
        self.assertEqual(res, 314.1593)

    def test_area_float(self):
        res = area(1.4)
        self.assertEqual(res, 6.1575)


    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_int(self):
        res = perimeter(10)
        self.assertEqual(res, 62.8319)

    def test_perimeter_float(self):
        res = perimeter(1.4)
        self.assertEqual(res, 8.7965)