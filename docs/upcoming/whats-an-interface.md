- [BW 5 mins] What's an interface?
    - https://miro.com/app/board/uXjVGdcuFEU=/?moveToWidget=3458764652062993479&cot=14

---

## Interfaces (ABC)

```python
import abc
import math
from typing import Protocol


class Shape2D(abc.ABC):
    @abc.abstractmethod
    def perimeter(self) -> float: ...
    @abc.abstractmethod
    def area(self) -> float: ...


class Circle(Shape2D):
    radius: float

    def __init__(self, radius: float):
        self.radius = radius

    def __repr__(self):
        return f"Circle(radius={self.radius!r})"

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Square(Shape2D):
    length: float

    def __init__(self, length: float):
        self.length = length

    def __repr__(self):
        return f"Square(length={self.length!r})"

    def perimeter(self):
        return 2 * self.length

    def area(self):
        return self.length ** 2


class EquilateralTriangle(Shape2D):
    length: float

    def __init__(self, length: float):
        self.length = length

    def __repr__(self):
        return f"Square(length={self.length!r})"

    # def perimeter(self):
    #     return 3 * self.length

    def area(self):
        return (self.length ** 2) * math.sqrt(3) / 4


def print_shape_details(shape: Shape2D):
    """
    Print the perimeter and area of a 2D-shape.
    """

    print(f"{repr(shape)}")
    print(f"  perimeter: {shape.perimeter():.4f}")
    print(f"  area: {shape.area():.4f}")


def pa_ratio(shape: Shape2D) -> float:
    """
    Return the perimeter-to-area ratio.
    """

    if shape.area() == 0:
        return math.inf
    else:
        return shape.perimeter() / shape.area()


class SomethingWithAnArea(Protocol):
    def area(self) -> float: ...


def total_area(*shapes: SomethingWithAnArea) -> float:
    """
    Return the total area of all shapes.
    """

    return sum(shape.area() for shape in shapes)


def main():
    circle = Circle(2)
    square = Square(2)
    # triangle = EquilateralTriangle(2)

    print_shape_details(circle)
    print_shape_details(square)
    # print_shape_details(triangle)

    print(f"circle PA ratio: {pa_ratio(circle)}")
    print(f"square PA ratio: {pa_ratio(square)}")
    print(f"triangle PA ratio: {pa_ratio(triangle)}")

    print("total area:", total_area(circle, square))
    print("total area:", total_area(circle, square, triangle))


if __name__ == "__main__":
    main()
```

## Interfaces (Protocol)

```python
# TODO: Add Rust example (with traits)

import math
from typing import Protocol


class Shape2D(Protocol):
    def perimeter(self) -> float: ...
    def area(self) -> float: ...


class Circle:
    radius: float

    def __init__(self, radius: float):
        self.radius = radius

    def __repr__(self):
        return f"Circle(radius={self.radius!r})"

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Square:
    length: float

    def __init__(self, length: float):
        self.length = length

    def __repr__(self):
        return f"Square(length={self.length!r})"

    def perimeter(self):
        return 4 * self.length

    def area(self):
        return self.length ** 2


class EquilateralTriangle:
    length: float

    def __init__(self, length: float):
        self.length = length

    def __repr__(self):
        return f"Square(length={self.length!r})"

    # def perimeter(self):
    #     return 3 * self.length

    def area(self):
        return (self.length ** 2) * math.sqrt(3) / 4


def print_shape_details(shape: Shape2D) -> None:
    """
    Print the perimeter and area of a 2D-shape.
    """

    print(f"{repr(shape)}")
    print(f"  perimeter: {shape.perimeter():.4f}")
    print(f"  area: {shape.area():.4f}")


def pa_ratio(shape: Shape2D) -> float:
    """
    Return the perimeter-to-area ratio.
    """

    if shape.area() == 0:
        return math.inf
    else:
        return shape.perimeter() / shape.area()


class SomethingWithAnArea(Protocol):
    def area(self) -> float: ...


def total_area(*shapes: SomethingWithAnArea) -> float:
    """
    Return the total area of all shapes.
    """

    return sum(shape.area() for shape in shapes)


def main():
    circle = Circle(2)
    square = Square(2)
    triangle = EquilateralTriangle(2)

    print_shape_details(circle)
    print_shape_details(square)
    # print_shape_details(triangle)

    print(f"circle PA ratio: {pa_ratio(circle)}")
    print(f"square PA ratio: {pa_ratio(square)}")
    # print(f"triangle PA ratio: {pa_ratio(triangle)}")

    print("total area:", total_area(circle, square, triangle))


if __name__ == "__main__":
    main()
```
