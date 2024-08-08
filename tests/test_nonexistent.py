import pytest
import allure

# This can be used for skipping some 
# lessons tests that are not implemented yet
docutils = pytest.importorskip("docutils")


parent_suite = "Suite 99: Ideas for the Future"

@allure.title("This is skipped; docutils is not installed.")
@allure.parent_suite(parent_suite)
def test_nonexistent():
    assert True