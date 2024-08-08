import allure
import math

from ml.utils.math import euclidean_distance

from test_config import suite_05 

@allure.title("Eucledian distance")
@allure.description("""
    The kNN has a dependency to the ml.utils.math.euclidean_distance function.
    This function should be implemented correctly.
""")
@allure.parent_suite(suite_05)
def test_euclidean_distance():
    p = [1, 2]
    q = [3, 4]
    assert euclidean_distance(p, q) == math.dist(p, q)

    p = [1, 2, 3, 4]
    q = [2, 2, 4, 4]
    assert euclidean_distance(p, q) == math.dist(p, q)