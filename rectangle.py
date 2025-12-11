def area(a, b):
    """Возвращает площадь прямоугольника"""
    if a<0 or b<0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b

def perimeter(a, b):
    """Возвращает периметр прямоугольника"""
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (a + b)
