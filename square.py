import unittest

def area(a):
    """
        Находит площадь квадрата и округляет по седьмому знаку, чтобы избежать проблем с неточностью float.

            Параметры:
                a (float): Сторона квадрата.

            Возвращаемое значение:
                area (float): Площадь квадрата.
    """
    return round(a * a, 7)


def perimeter(a):
    """
        Находит периметр квадрата и округляет по седьмому знаку, чтобы избежать проблем с неточностью float.

            Параметры:
                a (float): Сторона квадрата.

            Возвращаемое значение:
                perimeter (float): Периметр квадрата.
    """
    return round(4 * a, 7)


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_int(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_float(self):
        res = area(1.4)
        self.assertEqual(res, 1.96)


    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_int(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_perimeter_float(self):
        res = perimeter(1.4)
        self.assertEqual(res, 5.6)