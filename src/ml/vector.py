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
        >>> v + 1
        Vector(2, 3, 4)
        >>> 1 + v
        Vector(2, 3, 4)
        >>> v - v2
        Vector(-3, -3, -3)
        >>> v - 1
        Vector(0, 1, 2)
        >>> 1 - v
        Vector(0, 1, 2)
        >>> v / 2
        Vector(0.5, 1.0, 1.5)
        >>> v * v2
        Vector(4, 10, 18)
        >>> v @ v2
        32
    """
    
    def __init__(self, *args: int|float):
        self.elements = list(args)
        print("Yo")

    @staticmethod
    def add(a: Vector, b: Vector) -> Vector:
        """
        Adds two vectors element-wise.
        """
        if len(a) != len(b):
            raise ValueError("Vectors must have the same length")
        result = [x + y for x, y in zip(a, b)]
        return Vector(*result)
    
    @staticmethod
    def sub(a: Vector, b: Vector) -> Vector:
        """
        Subtracts two vectors element-wise.
        """
        if len(a) != len(b):
            raise ValueError("Vectors must have the same length")
        result = [x - y for x, y in zip(a, b)]
        return Vector(*result)

    @staticmethod
    def add_scalar(a, b):
        result = [x + b for x in a.elements]
        return Vector(*result)
    
    @staticmethod
    def sub_scalar(a, b):
        result = [x - b for x in a.elements]
        return Vector(*result)
    
    def _check_len_match(self, other: Vector):
        if len(self) != len(other):
            raise ValueError("Vectors must have the same length")

    def __add__(self, other):
        if isinstance(other, Vector):
            self._check_len_match(other)
            return self.add(self, other)
        # If int or float
        if isinstance(other, (int, float)):
            return self.add_scalar(self, other)
        else:
            raise NotImplementedError(f"Addition not supported for Vector and {type(other)}")
        
    def __radd__(self, other):
        return self.__add__(other)
        
    def __sub__(self, other):
        if isinstance(other, Vector):
            self._check_len_match(other)
            return self.sub(self, other)
        if isinstance(other, (int, float)):
            return self.sub_scalar(self, other)
        else:
            raise NotImplementedError(f"Subtraction not supported for Vector and {type(other)}")
        
    def __rsub__(self, other):
        return self.__sub__(other)
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            result = [x / other for x in self.elements]
            return Vector(*result)
        else:
            raise NotImplementedError(f"Division not supported for Vector and {type(other)}")
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = [x * other for x in self]
            return Vector(*result)
        if isinstance(other, Vector):
            self._check_len_match(other)
            result = [x * y for x, y in zip(self, other)]
            return Vector(*result)
        else:
            raise NotImplementedError(f"Multiplication not supported for Vector and {type(other)}")
        
    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __matmul__(self, other):
        if isinstance(other, Vector):
            self._check_len_match(other)
            return sum(self * other)
        else:
            raise NotImplementedError(f"Matrix multiplication not supported for Vector and {type(other)}")
        
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            result = [x ** other for x in self]
            return Vector(*result)
        else:
            raise NotImplementedError(f"Power not supported for Vector and {type(other)}")
    
    def __len__(self):
        return len(self.elements)
    
    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        return self.elements == other.elements

    def __iter__(self):
        return iter(self.elements)
    
    def __repr__(self):
        return f"Vector({', '.join(map(str, self.elements))})"
    
    def __str__(self):
        return f"({', '.join(map(str, self.elements))})"

if __name__ == "__main__":
    import doctest
    doctest.testmod()