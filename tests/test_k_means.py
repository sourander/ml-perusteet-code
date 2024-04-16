import os
import importlib
import allure

import ml.k_means as km

from test_config import lesson_06 as parent_suite

@allure.title("Data to Points")
@allure.description("""
    The kMeans class should be able to convert a list of tuples to a list of Points.
    Each Point should contain the original coordinates and a cluster_id of -1.
""")
@allure.parent_suite(parent_suite)
def test_data_to_points():
    data = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (10, 11, 12),
    ]

    points = km.kMeans.data_to_points(data)
    assert isinstance(points[0], km.Point)
    assert len(points) == len(data)
    assert points[0].coordinates == (1, 2, 3)
    assert points[0].cluster_id == -1


@allure.title("Mean of Points")
@allure.description("""
    The kMeans class should be able to calculate the mean of a list of Points.
    The mean should be a tuple of the average of each coordinate.
""")
@allure.parent_suite(parent_suite)
def test_mean_of_points():
    data = ([1, 2], [2, 3], [3, 4])
    assert km.kMeans.mean_coordinates(data) == [2.0, 3.0]

    data = ([1, 2, 3], [2, 3, 4], [3, 4, 5])
    assert km.kMeans.mean_coordinates(data) == [2.0, 3.0, 4.0]


@allure.title("Fit the Model")
@allure.parent_suite(parent_suite)
def test_fit_model():
    data = [
        (1.1, 2.1, 3.1),
        (1.2, 2.2, 3.2),
        (4.1, 5.1, 6.1),
        (4.2, 5.2, 6.2),
        (10.1, 11.1, 12.1),
        (10.2, 11.2, 12.2),
    ]

    model = km.kMeans(3)
    model.fit(data)

    assert model._is_converged
    assert model._converted_reason == "All centroids have converged"

