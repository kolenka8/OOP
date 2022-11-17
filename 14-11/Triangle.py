"""Файл с классом."""

class NotValidTriangle(Exception):
    """Такого треугольника не существует."""
    pass

class Triangle:
    '''Класс для геометрической фигуры - треугольник.'''

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        """Инициализирует трегольник.
        Args:
            side_a: float - длина первой стороны.
            side_b: float - длина второй стороны.
            side_c: float - длина третьей стороны.
        Raises:
            NotValidTriangle: можно ли построить треугольник.
        """
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not self.is_valid():
            raise NotValidTriangle
 
    def find_square(self) -> float:
        """Считает площадь треугольника.
        Returns:
            float: Площадь треугольника
        """
        p = (self.side_a + self.side_b + self.side_c) / 2
        return round((p*(p - self.side_a)*(p - self.side_b)*(self.side_c))**0.5, 2)

    def find_perimetr(self) -> float:
        """Считает периметр треугольника.
        Returns:
            float: Периметр треугольника
        """
        return round(self.side_a + self.side_b + self.side_c, 2)
    def is_valid(self) -> bool:
        """Проверка, существует ли такой треугольник.
        Returns:
            bool: результат проверки
        """
        sides = sorted([self.side_a, self.side_b, self.side_c])
        for side in sides:
            if not isinstance(side, float):
                return False
            if side <= 0:
                return False
        if sides[0] > sides[1] + sides[2]:
            return False
        return True


tr = Triangle(.2, .2, .2)
print(tr.find_perimetr())