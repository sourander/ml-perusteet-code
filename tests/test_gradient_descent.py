import allure
import random

from test_config import suite_08 as parent_suite
from ml.gradient_descent import GradientDescent
from ml.vector import Vector


@allure.title("Test predicting with lesson weights")
@allure.parent_suite(parent_suite)
def test_gradient_descent_fit():
    # These values are from the lesson Mkdocs material
    X = [Vector(x) for x in range(8)]
    y = Vector(*[1.52,  1.24,  1.03,  0.83,  0.49,  0.24,  0.08, -0.21])

    model = GradientDescent()
    model.X = model._add_bias(X)
    model.y, model.m = y, len(y)
    model.w = Vector(-0.5, 0.5) # Hard coded to match the slides
    assert model.predict(model.X, model.w) == Vector(-0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0)
    assert 3.274 < model.loss(model.X, model.w) < 3.276
    assert 1.19 < model.gradient()[0] < 1.195
    assert 12.0 < model.gradient()[1] < 12.02

@allure.title("Test fitting with random weights")
@allure.parent_suite(parent_suite)
def test_gradient_descent_fit_random():

    # These values are from the lesson Mkdocs material
    X = [Vector(x) for x in range(8)]
    y = Vector(*[1.52,  1.24,  1.03,  0.83,  0.49,  0.24,  0.08, -0.21])

    model = GradientDescent(learning_rate = 0.01, max_iterations = 1000)
    model.fit(X, y)
    assert 0.0 < model.loss(model.X, model.w) < 0.01
    assert 1.51 < model.w[0] < 1.52
    assert -0.24 > model.w[1] > -0.25