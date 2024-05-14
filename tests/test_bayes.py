import allure

from ml.naive_bayes import NaiveBayes

from test_config import lesson_02 as parent_suite

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
        ("free viagra now", 1),                 # Spam
        ("viagra for a limited time only", 1),  # Spam
        ("a game of golf tomorrow", 0),
        ("office movie night cancelled", 0),
        ("tldr newsletter", 0),
        ("a cat for sale", 0),
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
    assert nb.predict("duck for dinner") == 0