import os
import importlib
import allure

import ml.decision_tree as dt

parent_suite = "Lesson 03: Decision Trees"

@allure.title("Tree with Uniform Class")
@allure.description("A simple, uniform test set should result in a Leaf node with a uniform class.")
@allure.parent_suite(parent_suite)
def test_build_tree_uniform_class():
    # Test when all samples have the same class
    data = [(1, 1), (1, 1), (0, 1)]
    tree = dt.build_tree(data)
    assert isinstance(tree, dt.Leaf)
    assert tree.exit_reason == "Uniform class"
    assert tree.label == 1

@allure.title("Tree with Bike Car Data")
@allure.parent_suite(parent_suite)
def test_build_tree_bike_car():
    data = [
        (0, 0, 10.63, 1),
        (1, 1, 71.09, 1),
        (0, 1, 42.95, 1),
        (1, 0, 24.53, 1),
        (1, 0, 53.66, 1),
        (0, 1, 71.79, 1),
        (1, 0, 5.88, 0),
        (1, 1, 57.5, 1),
        (0, 0, 25.32, 1),
        (1, 0, 34.39, 1),
        (1, 1, 56.91, 1),
        (1, 0, 64.6, 1),
        (1, 1, 17.46, 0),
        (0, 1, 87.61, 1),
        (1, 0, 14.2, 1),
        (1, 1, 8.28, 0)
    ]

    tree = dt.build_tree(data, verbose=False)
    assert isinstance(tree, dt.Decision)
    assert tree.ig.column_index == 2 # First split should be on speed

    # Test three predictions
    assert dt.predict(tree, [1, 1, 25.0]) == 1 # Speed > 20 -> Car
    assert dt.predict(tree, [1, 0, 17.5]) == 1 # Not well rested, speed > 15 -> Car
    assert dt.predict(tree, [0, 0, 10.0]) == 1 # No shower, speed > 10 -> Car


@allure.title("Class Probabilities")
@allure.parent_suite(parent_suite)
def test_class_probabilities():
    # Test when all samples have the same class
    data = [1, 1, 1, 0, 0, 0]
    assert dt.class_probabilities(data) == [0.5, 0.5]

    data = [1, 1, 1, 1, 1, 1]
    assert dt.class_probabilities(data) == [0.0, 1.0]

    data = [1, 1, 1, 1, 1, 1, 0, 0]
    assert dt.class_probabilities(data) == [0.25, 0.75]


@allure.title("Entropy")
@allure.parent_suite(parent_suite)
def test_entropy():
    assert dt.entropy([0.5, 0.5]) == 1.0
    assert dt.entropy([0.0, 1.0]) == 0.0
    assert 0.97 < dt.entropy([0.6, 0.4]) < 0.98