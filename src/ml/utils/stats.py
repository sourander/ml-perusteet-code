from ml.vector import Vector

def mean(x: Vector):
    return sum(x) / len(x)

def variance(x: Vector, ddof=1):
    return sum((x - mean(x))**2) / (len(x) - ddof)

def std(x: Vector):
    return variance(x, ddof=0) ** 0.5

def center(x: Vector):
    return x - mean(x)

def z_score(x: Vector):
    return center(x) / std(x)

def min_max(x: Vector):
    return (x - min(x)) / (max(x) - min(x))