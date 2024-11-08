import math


class Vector:
    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(round(self.x * other, 2), round(self.y * other, 2))
        elif isinstance(other, Vector):
            # Округляємо до 4 знаків після коми для відповідності тестам
            return round(self.x * other.x + self.y * other.y, 5)
        else:
            raise ValueError("Multiplication with non-numeric or non-Vector type is not supported")

    @classmethod
    def create_vector_by_two_points(cls, start_point, end_point):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other):
        dot_product = self * other
        len_self = self.get_length()
        len_other = other.get_length()
        if len_self == 0 or len_other == 0:
            raise ValueError("Angle is undefined for zero-length vector")
        cos_a = dot_product / (len_self * len_other)
        cos_a = max(-1, min(1, cos_a))  # Кліпінг значення для коректності
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def get_angle(self):
        # Відлік кута від позитивної осі Y
        angle = math.degrees(math.atan2(self.y, self.x))
        angle_from_y = (450 - angle) % 360  # Відрахунок від осі Y за годинниковою стрілкою
        return round(angle_from_y)

    def rotate(self, degrees):
        radians = math.radians(degrees)
        new_x = self.x * math.cos(radians) - self.y * math.sin(radians)
        new_y = self.x * math.sin(radians) + self.y * math.cos(radians)
        return Vector(round(new_x, 2), round(new_y, 2))
