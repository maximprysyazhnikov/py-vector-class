import math


class Vector:
    def __init__(self, end_x: float, end_y: float) -> None:
        """Ініціалізація вектора з координатами кінцевої точки."""
        self.end_x = end_x
        self.end_y = end_y

    def __add__(self, other: "Vector") -> "Vector":
        """Метод для додавання двох векторів."""
        if not isinstance(other, Vector):
            raise ValueError("Operand must be a Vector.")
        return Vector(self.end_x + other.end_x, self.end_y + other.end_y)

    def __sub__(self, other: "Vector") -> "Vector":
        """Метод для віднімання двох векторів."""
        if not isinstance(other, Vector):
            raise ValueError("Operand must be a Vector.")
        return Vector(self.end_x - other.end_x, self.end_y - other.end_y)

    def __mul__(self, other: "Vector") -> float:
        """Метод для обчислення скалярного добутку двох векторів."""
        if not isinstance(other, Vector):
            raise ValueError("Operand must be a Vector.")
        return self.end_x * other.end_x + self.end_y * other.end_y

    def scalar_multiply(self, number: float) -> "Vector":
        """Метод для множення вектора на скаляр."""
        if not isinstance(number, (int, float)):
            raise ValueError("Operand must be a number.")
        return Vector(self.end_x * number, self.end_y * number)

    def get_angle(self) -> float:
        """Метод для обчислення кута вектора від осі X в радіанах."""
        angle = math.atan2(self.end_y, self.end_x)
        return math.degrees(angle)  # Перетворення з радіан в градуси

    def get_normalized(self) -> "Vector":
        """Метод для нормалізації вектора."""
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return self.scalar_multiply(1 / magnitude)

    def magnitude(self) -> float:
        """Метод для обчислення довжини (модулю) вектора."""
        return math.sqrt(self.end_x ** 2 + self.end_y ** 2)

    def rotate(self, angle_degrees: float) -> "Vector":
        """Метод для обертання вектора на заданий кут в градусах."""
        angle_radians = math.radians(angle_degrees)  # Перетворення в градуси
        cos_angle = math.cos(angle_radians)
        sin_angle = math.sin(angle_radians)
        new_x = self.end_x * cos_angle - self.end_y * sin_angle
        new_y = self.end_x * sin_angle + self.end_y * cos_angle
        return Vector(new_x, new_y)

    @classmethod
    def create_from_two_points(cls, start_point: tuple, end_point: tuple) -> "Vector":
        """Метод для створення вектора з двох точок."""
        start_x, start_y = start_point
        end_x, end_y = end_point
        return cls(end_x - start_x, end_y - start_y)

    def __repr__(self) -> str:
        """Метод для репрезентації об'єкта."""
        return f"Vector({self.end_x}, {self.end_y})"
