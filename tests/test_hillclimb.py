import allure
import random

from test_config import suite_07 as parent_suite
from ml.hill_climb import HillClimb, Solution

X = [
    [-0.84, -1.12], 
    [-1.11, -2.36], 
    [-0.96, -0.75], 
    [-1.4, 1.3], 
    [1.86, -0.19], 
    [0.67, 1.59], 
    [-0.22, 1.48], 
    [-0.9, -0.09], 
    [-1.15, 0.77], 
    [-0.51, -0.6]
]
y = [-117.0, -225.09, -92.35, 56.07, 47.31, 149.73, 110.69, -37.88, 23.01, -65.43]

@allure.title("Test fitting the HillClimb model")
@allure.parent_suite(parent_suite)
def test_hillclimb_fit():
    model = HillClimb()
    model.fit(X, y)

    assert model.best_solution is not None, "The model should store the best solution after fitting"
    assert isinstance(model.best_solution, Solution), "The best solution should be an instance of the Solution class"
    
    assert model.best_solution.iterations > 0, "The number of iterations should be greater than 0"
    assert 0 < model.best_solution.loss < 0.3, "The loss should be a fairly small value (e.g. 0.14)"

@allure.title("Test predicting with the HillClimb model")
@allure.parent_suite(parent_suite)
def test_hillclimb_predict():
    model = HillClimb()
    model.fit(X, y)

    # Create test data that is like the original X, but with small randomness
    # Added to each element. Proper amount of randomness is less than +/- 0.1
    X_test = [[x + random.uniform(-0.01, 0.01) for x in row] for row in X]

    y_hat = model.predict(X_test)

    # Check that each y is within a reasonable range
    reasonable_range = 3
    for i, y_i in enumerate(y_hat):
        assert abs(y_i - y[i]) < reasonable_range, f"Prediction {y_i} is too far from original {y[i]} (Reasonable range being {reasonable_range})"



