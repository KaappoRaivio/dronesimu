from __future__ import annotations

from math import radians, sin, cos, sqrt
import numbers
from typing import Union


class Vector3D:
    def __init__(self, i, j, k):
        self.__i = i
        self.__j = j
        self.__k = k

    def __str__(self) -> str:
        return f"({self.__i:.2f}i + {self.__j:.2f}j + {self.__k:.2f}k)"

    def __add__(self, other) -> Vector3D:
        return Vector3D(self.i + other.i, self.j + other.j, self.k + other.k)

    def __neg__(self):
        return Vector3D(-self.i, -self.j, -self.k)

    def __sub__(self, other):
        return self + -other

    def __abs__(self):
        return sqrt(self.i ** 2 + self.j ** 2 +self.k ** 2)

    def __mul__(self, other) -> Union[Vector3D, int]:
        if isinstance(other, Vector3D):
            return self.i * other.i + self.j * other.j + self.k * other.k
        elif isinstance(other, numbers.Number):
            return Vector3D(self.i * other, self.j * other, self.k * other)
        else:
            raise Exception(f"Unsupported operand {other}!")

    def __truediv__(self, other):
        return Vector3D(self.i / other, self.j / other, self.k / other)

    def normalize(self):
        return self / abs(self)

    def bad_euler_to_sphere_coords(self) -> Vector3D:
        a = radians(self.__i)
        b = radians(self.__j)
        return Vector3D(sin(a) * cos(b), sin(b), cos(a) * cos(b))

    @property
    def i(self):
        return self.__i

    @property
    def j(self):
        return self.__j

    @property
    def k(self):
        return self.__k


class PositionalVector3D:
    def __init__(self, vector, position=Vector3D(0, 0, 0)):
        self.__vector = vector + position
        self.__position = position

    def __add__(self, other):
        result = self.vector + other
        return PositionalVector3D(result, self.position)


    def __neg__(self):
        return PositionalVector3D(-self.vector, self.position)

    def __sub__(self, other):
        result = self.vector - other
        return PositionalVector3D(result, self.position)

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return PositionalVector3D(self.vector * other, self.position)
        elif isinstance(other, Vector3D):
            return self.vector * other

    def __abs__(self):
        return abs(self.vector)

    def __str__(self):
        return f"{self.vector} at {self.position}"

    def normalize(self):
        return PositionalVector3D(self.vector.normalize(), self.position)

    def __iter__(self):
        yield (self.position.i, self.vector.i,)
        yield (self.position.j, self.vector.j,)
        yield (self.position.k, self.vector.k,)

    @property
    def vector(self):
        return self.__vector

    @property
    def position(self):
        return self.__position


if __name__ == "__main__":
    print(PositionalVector3D(Vector3D(0, 0, 1)) - Vector3D(1, 1, 1))