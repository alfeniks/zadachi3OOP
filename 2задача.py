class Point:
    def __init__(self, x=0, y=0):
        """Конструктор для инициализации координат точки."""
        self.x = x
        self.y = y

    def set_coordinates(self, x, y):
        """Метод для изменения координат точки."""
        self.x = x
        self.y = y

    def get_coordinates(self):
        """Метод для получения текущих координат точки."""
        return (self.x, self.y)

    def distance_to(self, other_point):
        """Метод для вычисления расстояния между текущей точкой и другой точкой."""
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return (dx**2 + dy**2) ** 0.5

    def __str__(self):
        """Метод для удобного вывода объекта точки."""
        return f"Point({self.x}, {self.y})"


# Пример использования класса Point
point1 = Point(3, 4)
point2 = Point(6, 8)

# Получаем координаты точек
print("Point 1 coordinates:", point1.get_coordinates())
print("Point 2 coordinates:", point2.get_coordinates())

# Изменяем координаты точки
point1.set_coordinates(1, 1)
print("Updated Point 1 coordinates:", point1.get_coordinates())

# Вычисляем расстояние между точками
distance = point1.distance_to(point2)
print("Distance between Point 1 and Point 2:", distance)

# Выводим информацию о точке с помощью __str__
print("Point 1:", point1)
