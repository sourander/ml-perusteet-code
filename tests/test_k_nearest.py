import allure
import ml.k_nearest as knn

from test_config import suite_05 as parent_suite

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