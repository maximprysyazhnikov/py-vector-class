import math
from typing import Tuple, Union


class Vector:
    def __init__(self, end_x: float, end_y: float) -> None:
        self.end_x = round(end_x, 2)
        self.end_y = round(end_y, 2)

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.end_x + other.end_x, self.end_y + other.end_y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.end_x - other.end_x, self.end_y - other.end_y)

    def __mul__(self, other: Union["Vector", float]) -> Union["Vector", float]:
        if isinstance(other, (int, float)):
            return Vector(
                round(self.end_x * other, 2),
                round(self.end_y * other, 2)
            )
        if isinstance(other, Vector):
            return round(
                self.end_x * other.end_x + self.end_y * other.end_y,
                5
            )
        raise ValueError("Multiplication with non-numeric or non-Vector type")

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: Tuple[float, float], end_point: Tuple[float, float]
    ) -> "Vector":
        end_x = end_point[0] - start_point[0]
        end_y = end_point[1] - start_point[1]
        return cls(end_x, end_y)

    def get_length(self) -> float:
        return math.sqrt(self.end_x ** 2 + self.end_y ** 2)

    def get_normalized(self) -> "Vector":
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(
            round(self.end_x / length, 2),
            round(self.end_y / length, 2)
        )

    def angle_between(self, other: "Vector") -> int:
        dot_product = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Angle is undefined for zero-length vector")
        cos_a = dot_product / (len_self * len_other)
        cos_a = max(-1, min(1, cos_a))
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self) -> int:
        angle = math.degrees(math.atan2(self.end_y, self.end_x))
        angle_from_y = (450 - angle) % 360
        return round(angle_from_y)

    def rotate(self, degrees: int) -> "Vector":
        radians = math.radians(degrees)
        new_x = self.end_x * math.cos(radians) - self.end_y * math.sin(radians)
        new_y = self.end_x * math.sin(radians) + self.end_y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
