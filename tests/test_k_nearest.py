import os
import importlib
import allure
import math

import ml.k_nearest as knn

parent_suite = "Lesson 05: k-Nearest Neighbors"

@allure.title("Eucledian distance")
@allure.parent_suite(parent_suite)
def test_euclidean_distance():
    p = [1, 2]
    q = [3, 4]
    assert knn.kNN.euclidean_distance(p, q) == math.dist(p, q)

    p = [1, 2, 3, 4]
    q = [2, 2, 4, 4]
    assert knn.kNN.euclidean_distance(p, q) == math.dist(p, q)

@allure.title("Majority vote")
@allure.parent_suite(parent_suite)
def test_majority_vote():
    neighbors = [
        knn.Neighbor(1.23, "cat"),
        knn.Neighbor(1.45, "dog"),
        knn.Neighbor(2.01, "cat"),
    ]
    assert knn.kNN.majority_vote(neighbors) == "cat"

@allure.title("Fit kNN")
@allure.parent_suite(parent_suite)
def test_fit():
    data = [
        (1, 2, 3, "cat"),
        (4, 5, 6, "cat"),
        (7, 8, 9, "dog"),
        (10, 11, 12, "dog"),
    ]
    k = 1
    model = knn.kNN(k=k)
    model.fit(data)
    assert len(model.points) == len(data)
    assert model.points[0].features == (1, 2, 3)
    assert model.points[0].label == "cat"
    assert model.k == k