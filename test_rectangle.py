# test_rectangle.py
import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    
    def test_area_normal(self):
        # Проверка нормальных значений
        self.assertEqual(area(5, 4), 20)
        self.assertEqual(area(3, 7), 21)
        self.assertEqual(area(2.5, 4), 10.0)
    
    def test_area_zero(self):
        # Проверка граничных значений
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 10), 0)
        self.assertEqual(area(0, 0), 0)
    
    def test_area_negative(self):
        # Проверка на отрицательные значения (если нужно)
        self.assertEqual(area(-5, 4), -20)
        # Или можно проверять исключения:
        # with self.assertRaises(ValueError):
        #area(-5, 4)
    
    def test_perimeter_normal(self):
        # Проверка периметра
        self.assertEqual(perimeter(5, 4), 18)
        self.assertEqual(perimeter(3, 7), 20)
        self.assertEqual(perimeter(2.5, 4), 13.0)
    
    def test_perimeter_zero(self):
        # Граничные значения для периметра
        self.assertEqual(perimeter(10, 0), 20)
        self.assertEqual(perimeter(0, 0), 0)

if __name__ == '__main__':
    unittest.main()