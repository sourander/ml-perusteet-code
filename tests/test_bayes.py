import os
import importlib
import allure

from ml.naive_bayes import NaiveBayes

parent_suite = "Lesson 02: Naive Bayes"

@allure.title("Test Word Processor")
@allure.description("The word processor should lowercase the word and remove any non-alphanumeric characters")
@allure.parent_suite(parent_suite)
def test_word_processor():
    assert NaiveBayes.preprocess_word("Viagra?!?") == "viagra"

@allure.title("Test Naive Bayes with Spam Evidence")
@allure.parent_suite(parent_suite)
def test_bayes_positive():
    nb = NaiveBayes()
    nb.fit([
        ("Viagra Viagra now", 1),      # Spam
        ("Now now Viagra", 1),         # Spam
        ("Nospam nospam nospam", 0),
        ("Egg egg egg egg", 0),
        ("ham ham ham ham", 0),
    ])
    assert nb.predict("free viagra movie") == 1

@allure.title("Test Naive Bayes with Not Spam Evidence")
@allure.parent_suite(parent_suite)
def test_bayes_negative():
    nb = NaiveBayes()
    nb.fit([
        ("Spam spam spam", 1),         # Spam
        ("One little duck", 0),
        ("No little ducks", 0),
    ])
    assert nb.predict("duck ducks") == 0