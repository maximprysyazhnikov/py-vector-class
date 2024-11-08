import math
from typing import Union, Tuple


class Vector:
    def __init__(self, x_coord: float, y_coord: float):
        self.x = x_coord
        self.y = y_coord

    def __add__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise ValueError("Operand must be a Vector.")

    def __sub__(self, other: "Vector") -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise ValueError("Operand must be a Vector.")

    def __mul__(self, other: Union["Vector", float, int]) -> Union["Vector", float]:
        if isinstance(other, Vector):
            return self.dot(other)
        elif isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        raise ValueError("Operand must be a Vector or a scalar.")

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def get_length(self) -> float:
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 2)

    def get_angle(self) -> float:
        return round(math.degrees(math.atan2(self.y, self.x)), 2)

    def angle_between(self, other: "Vector") -> float:
        if not isinstance(other, Vector):
            raise ValueError("Operand must be a Vector.")

        dot_product = self.dot(other)
        magnitude1 = self.get_length()
        magnitude2 = other.get_length()

        cosine_theta = dot_product / (magnitude1 * magnitude2)
        cosine_theta = max(-1, min(1, cosine_theta))
        return round(math.degrees(math.acos(cosine_theta)), 2)

    def dot(self, other: "Vector") -> float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise ValueError("Operand must be a Vector.")

    @classmethod
    def from_points(cls, start_point: Tuple[float, float], end_point: Tuple[float, float]) -> "Vector":
        return cls(end_point[0] - start_point[0], end_point[1] - start_point[1])

    def normalize(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def rotate(self, angle: float) -> "Vector":
        angle_rad = math.radians(angle)
        new_x = self.x * math.cos(angle_rad) - self.y * math.sin(angle_rad)
        new_y = self.x * math.sin(angle_rad) + self.y * math.cos(angle_rad)
        return Vector(round(new_x, 2), round(new_y, 2))

    def get_normalized(self) -> "Vector":
        return self.normalize()
