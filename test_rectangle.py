import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    
    # Тесты для площади
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
    
    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_area_normal(self):
        res = area(3, 7)
        self.assertEqual(res, 21)
    
    def test_area_float(self):
        res = area(5.5, 2)
        self.assertEqual(res, 11.0)
    
    # Тесты для периметра
    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)
    
    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    
    def test_perimeter_normal(self):
        res = perimeter(3, 7)
        self.assertEqual(res, 20)
    
    def test_perimeter_float(self):
        res = perimeter(5.5, 2.5)
        self.assertEqual(res, 16.0)
    
    # Негативные тесты (ожидаем исключение)
    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-10, 5)
    
    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-10, -5)

if __name__ == "__main__":
    unittest.main()