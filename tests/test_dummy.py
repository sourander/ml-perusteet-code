import os
import importlib
import allure

from ml import kissa

parent_suite = "Lesson 00: Introduction to Pytest"

@allure.title("Test that 42 is returned")
@allure.parent_suite(parent_suite)
def test_dummy():
    a = kissa.return_42()
    assert 42 == a

@allure.title("Test that True is truly True")
@allure.parent_suite(parent_suite)
def test_another():
    assert True
