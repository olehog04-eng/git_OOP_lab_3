import math

class Figure:
    def dimension(self):
        return None
    def perimeter(self):
        return None
    def square(self):
        return None
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        return None

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
    def is_valid(self):
        return (self.__a > 0 and self.__b > 0 and self.__c > 0 and
            self.__a + self.__b > self.__c and
            self.__a + self.__c > self.__b and
            self.__b + self.__c > self.__a)
    def dimension(self):
        return 2
    def perimeter(self):
        return self.__a + self.__b + self.__c
    def square(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))
    def volume(self):
        return self.square()

class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def is_valid(self):
        return self.__a > 0 and self.__b > 0
    def dimension(self):
        return 2
    def square(self):
        return self.__a * self.__b
    def volume(self):
        return self.square()
    def get_a(self):
        return self.__a
    def get_b(self):
        return self.__b

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
    def is_valid(self):
        return min(self.__a, self.__b, self.__c, self.__d) > 0 and self.__a != self.__b
    def dimension(self):
        return 2
    def square(self):
        denom = 2 * (self.__a - self.__b)
        if denom == 0:
            return None
        x = (self.__a - self.__b + self.__c**2 - self.__d**2) / denom
        val = self.__c**2 - x**2
        if val <= 0:
            return None
        h = math.sqrt(val)
        return (self.__a + self.__b) * h / 2
    def volume(self):
        s = self.square()
        return s if s is not None else None

class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.__a = a
        self.__b = b
        self.__h = h
    def is_valid(self):
        return self.__a > 0 and self.__b > 0 and self.__h > 0
    def dimension(self):
        return 2
    def square(self):
        return self.__a * self.__h
    def volume(self):
        return self.square()

class Circle(Figure):
    def __init__(self, r):
        self.__r = r
    def is_valid(self):
        return self.__r > 0
    def dimension(self):
        return 2
    def square(self):
        return math.pi * self.__r ** 2
    def volume(self):
        return self.square()
    def get_radius(self):
        return self.__r

class Ball(Figure):
    def __init__(self, r):
        self.__r = r
    def is_valid(self):
        return self.__r > 0
    def dimension(self):
        return 3
    def volume(self):
        return (4 / 3) * math.pi * self.__r ** 3

class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.__h = h
    def is_valid(self):
        return super().is_valid() and self.__h > 0
    def dimension(self):
        return 3
    def volume(self):
        return super().square() * self.__h / 3

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.__c = c
    def is_valid(self):
        return super().is_valid() and self.__c > 0
    def dimension(self):
        return 3
    def volume(self):
        return super().square() * self.__c

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.__h = h
    def is_valid(self):
        return super().is_valid() and self.__h > 0
    def dimension(self):
        return 3
    def volume(self):
        return super().square() * self.__h

class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.__h = h
    def is_valid(self):
        return super().is_valid() and self.__h > 0
    def dimension(self):
        return 3
    def volume(self):
        return super().square() * self.__h / 3

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.__h = h
    def is_valid(self):
        return super().is_valid() and self.__h > 0
    def dimension(self):
        return 3
    def volume(self):
        return super().square() * self.__h / 3

def create_figure(line):
    data = line.split()
    name = data[0]
    params = list(map(float, data[1:]))
    mapping = {
        "Triangle": Triangle,
        "Rectangle": Rectangle,
        "Trapeze": Trapeze,
        "Parallelogram": Parallelogram,
        "Circle": Circle,
        "Ball": Ball,
        "Cone": Cone,
        "RectangularParallelepiped": RectangularParallelepiped,
        "TriangularPrism": TriangularPrism,
        "TriangularPyramid": TriangularPyramid,
        "QuadrangularPyramid": QuadrangularPyramid}
    if name not in mapping:
        return None
    obj = mapping[name](*params)
    if hasattr(obj, "is_valid") and not obj.is_valid():
        return None
    v = obj.volume()
    if v is None:
        return None
    return obj

figures = []

files = ["input01.txt", "input02.txt", "input03.txt"]
for file_name in files:
    figures = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            fig = create_figure(line)
            if fig is not None:
                figures.append(fig)
    if not figures:
        print("У файлі", file_name, "немає коректно заданих фігур")
    else:
        max_figure = max(figures, key=lambda f: f.volume())
        print("\nФайл:", file_name)
        print("Фігура:", type(max_figure).__name__)
        print("Виміри:", max_figure.volume())
