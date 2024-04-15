import allure

from ml.vector import Vector

parent_suite = "Lesson 01: Do-It-Yourself Vector"

@allure.title("Vector Addition")
@allure.parent_suite(parent_suite)
def test_vector_addition():
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    result = v1 + v2
    assert result == Vector(5, 7, 9)

@allure.title("Vector and Scalar Addition")
@allure.parent_suite(parent_suite)
def test_vector_scalar_addition():
    v = Vector(1, 2, 3)
    scalar = 5
    result = v + scalar
    assert result.elements == [6, 7, 8]

@allure.title("Vector Length")
@allure.parent_suite(parent_suite)
def test_vector_length():
    v = Vector(1, 2, 3)
    result = len(v)
    assert result == 3

@allure.title("Vector as Iterable")
@allure.parent_suite(parent_suite)
def test_vector_as_iterable():
    v = Vector(1, 2, 3)
    result = list(v)
    assert result == [1, 2, 3]