import unittest

def area(a, b):
    """
        Находит площадь прямоугольника и округляет по седьмому знаку, чтобы избежать проблем с неточностью float.

            Параметры:
                a (float): Первая сторона прямоугольника.
                b (float): Вторая сторона прямоугольника.

            Возвращаемое значение:
                area (float): Площадь прямоугольника.
    """
    return round(a * b, 10)

def perimeter(a, b):
    """
        Находит периметр прямоугольника и округляет по седьмому знаку, чтобы избежать проблем с неточностью float.

            Параметры:
                a (float): Первая сторона прямоугольника.
                b (float): Вторая сторона прямоугольника.

            Возвращаемое значение:
                perimeter (float): Периметр прямоугольника.
    """
    return round(2*(a + b),7)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_int(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_float(self):
        res = area(1.4, 1.7)
        self.assertEqual(res, 2.38)


    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_perimeter_int(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_float(self):
        res = perimeter(1.4, 1.7)
        self.assertEqual(res, 6.2)