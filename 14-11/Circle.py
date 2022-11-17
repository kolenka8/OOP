"""Файл с классом."""

import math

class NotValidCircle(Exception):
    """Такого круга не существует."""
    pass

class Circle:
    '''Класс для геометрической фигуры - круг.'''

    def __init__(self, radius: float) -> None:
        """Инициализирует круг.
        Args:
            radius: float - радиус круга.
        Raises:
            NotValidCircle: можно ли построить круг.
        """
        self.radius = radius
        if not self.is_valid():
            raise NotValidCircle

    def dlina(self) -> float:
        """Считает длину круга.
        Returns:
            float: Длина окружности
        """
        return round(2 * math.pi * self.radius, 2)
    
    def square(self) -> float:
        """Считает площадь круга.
        Returns:
            float: Площадь круга
        """
        return round(math.pi * self.radius ** 2, 2)
    def is_valid(self) -> bool:
        """Проверка, существует ли такой круг.
        Returns:
            bool: результат проверки
        """
        if isinstance(self.radius, (float)):
            return self.radius > 0
    