import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """Абстрактная фигура"""
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Такого треугольника не существует")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def is_right(self) -> bool:
        x, y, z = sorted([self.a, self.b, self.c])
        return math.isclose(z**2, x**2 + y**2)
