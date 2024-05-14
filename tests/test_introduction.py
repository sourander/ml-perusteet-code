import allure

from test_config import lesson_00 as parent_suite

@allure.title("True is True")
@allure.description("This test is always true. It is used to check that the test suite is working as expected. If it it, you are ready to start working on the exercises.")
@allure.parent_suite(parent_suite)
def test_another():
    assert True
