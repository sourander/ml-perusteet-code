from __future__ import annotations

class Vector:
    """
    A simple class to represent a vector in n-dimensional space.

    Attributes:
        vector: A list of numbers representing the vector.

    Examples:
        >>> v = Vector(1, 2, 3)
        >>> len(v)
        3
        >>> v2 = Vector(4, 5, 6)
        >>> v + v2
        Vector(5, 7, 9)
    
    """
    def __init__(self, *args: int|float):
        self.elements = list(args)

    @staticmethod
    def add(a: Vector, b: Vector) -> Vector:
        """
        Adds two vectors element-wise.
        """
        if len(a) != len(b):
            raise ValueError("Vectors must have the same length")
        result = [x + y for x, y in zip(a.elements, b.elements)]
        return Vector(*result)

    @staticmethod
    def add_scalar(a, b):
        result = [x + b for x in a.elements]
        return Vector(*result)

    def __add__(self, other):
        if isinstance(other, Vector):
            return self.add(self, other)
        # If int or float
        if isinstance(other, (int, float)):
            return self.add_scalar(self, other)
        else:
            raise NotImplementedError(f"Addition not supported for Vector and {type(other)}")
    
    def __len__(self):
        return len(self.elements)
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.elements == other.elements

    def __iter__(self):
        return iter(self.elements)

if __name__ == "__main__":
    import doctest
    doctest.testmod()