'''Классы Геометрических Фигур'''
import math

class Circle:
    '''Класс для геометрической фигуры - круг.'''

    def __init__(self, radius: float) -> None:
        """Создаёт круг.
        Args:
            radius: float - радиус круга.
        """
        self.radius = radius

    def dlina(self) -> float:
        """Считает длину.
        Returns:
            float: Длина окружности
        """
        return 2 * math.pi * self.radius
    
    def square(self) -> float:
        """Считает площадь.
        Returns:
            float: Площадь круга
        """
        return math.pi * self.radius ** 2

class Triangle:
    '''Класс для геометрической фигуры - треугольник.'''

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        """Создаёт трегольник.
        Args:
            side_a: float - длина первой стороны.
            side_b: float - длина второй стороны.
            side_c: float - длина третьей стороны.
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    
    def find_square(self) -> float:
        """Считает площадь.
        Returns:
            float: Площадь треугольника
        """
        p = (self.side_a + self.side_b + self.side_c) / 2
        return (p*(p - self.side_a)*(p - self.side_b)*(self.side_c))**0.5 

    def find_perimetr(self) -> float:
        """Считает периметр.
        Returns:
            float: Периметр треугольника
        """
        return self.side_a + self.side_b + self.side_c
