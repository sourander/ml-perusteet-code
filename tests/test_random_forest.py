import allure

import ml.random_forest as rf
from test_config import suite_04 as parent_suite

@allure.title("Bagging (with Replacement)")
@allure.parent_suite(parent_suite)
def test_sample_with_replacement():
    data = list(range(100))
    result = rf.sample_with_replacement(data)
    assert set(result) < set(data), "Replacement should introduce duplicates"
    assert len(result) == len(data), "Replacement should not change the length"

@allure.title("Bagging (without Replacement)")
@allure.parent_suite(parent_suite)
def test_sample_without_replacement():
    data = [1, 2, 3, 4, 5]
    n = 3
    result = rf.sample_without_replacement(data, n)
    assert len(result) == n, "Random sample should have the specified length"
    assert len(set(result)) == len(result), "Random sample should not contain duplicates"

@allure.title("Train Random Forest")
@allure.parent_suite(parent_suite)
def test_train():
    data = [
        (1, 19.2, 1), 
        (1, 19.4, 1),
        (0, 19.3, 1), 
        (1, 12.7, 1),
        (0, 12.1, 0), 
        (0, 13.1, 0),
    ]
    num_trees = 3
    model = rf.RandomForest(num_trees)
    model.train(data)
    assert len(model.trees) == num_trees
    # assert isinstance(model.trees[0], rf.dt.Decision), "The first Node in the forest should be a Decision Node, not a Leaf"
    # Instead, let's check that ALL THREE trees must not be leaves. One can be, due to randomization, or two. Three would be unlikely.
    assert sum([isinstance(tree, rf.dt.Decision) for tree in model.trees]) > 1, "The first Node in the forest should be a Decision Node, not a Leaf. None of the trained {num_trees} trees filled this requirement."

@allure.title("Predict using Random Forest")
@allure.parent_suite(parent_suite)
def test_predict():
    data = [
        (1, 19.2, 1), 
        (1, 19.4, 1),
        (0, 19.3, 1), 
        (1, 12.7, 1),
        (0, 12.1, 0), 
        (0, 13.1, 0),
    ]
    num_trees = 3
    model = rf.RandomForest(num_trees)
    model.train(data)
    sample = (1, 19.3)
    result = model.predict(sample)
    assert result == 1, f"Expected 1, got {result}"


