class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return sum(self.a, self.b)
    def __sub__(self, other):
        return self.a - self.b
    def __mul__(self, other):
        return self.a * self.b
    def __truediv__(self, other):
        return self.a / self.b

