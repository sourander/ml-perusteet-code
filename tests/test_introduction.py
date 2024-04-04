import os
import importlib
import allure

from ml import kissa

parent_suite = "Lesson 00: Introduction to Pytest and Allure"

@allure.title("True is True")
@allure.description("This test is always true. It is used to check that the test suite is working as expected. If it it, you are ready to start working on the exercises.")
@allure.parent_suite(parent_suite)
def test_another():
    assert True
