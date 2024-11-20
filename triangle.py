import unittest

def area(a, h):
    """
        Находит площадь треугольника и округляет по седьмому знаку, чтобы избежать проблем с неточностью float.

            Параметры:
                a (float): Сторона треугольника, к которой преведена высота.
                h (float): Высота треугольника.

            Возвращаемое значение:
                area (float): Площадь треугольника.
    """
    return round(a * h / 2, 7)

def perimeter(a, b, c):
    """
       Находит площадь треугольника и округляет по седьмому знаку, чтобы избежать проблем с неточностью float.

           Параметры:
               a (float): Первая сторона треугольника.
               b (float): Вторая сторона треугольника.
               c (float): Третья сторона треугольника.


           Возвращаемое значение:
               perimeter (float): Периметр треугольника.
   """
    return round(a + b + c, 7)


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    def test_area_zero(self):
        res = area(0, 10)
        self.assertEqual(res, 0)
    def test_area_int(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_area_float(self):
        res = area(1.4, 1.7)
        self.assertEqual(res, 1.19)


    def test_perimeter_zero(self):
        res = perimeter(10, 0, 5)
        self.assertEqual(res, 15)

    def test_perimeter_int(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_perimeter_float(self):
        res = perimeter(1.4, 1.7, 0.9)
        self.assertEqual(res, 4)