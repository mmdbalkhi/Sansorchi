"""Testing Sansorchi package"""
from sansorchi import data, sansor


def test_word():
    """Unit test, Clean the code with the help of pylint"""
    swears = data.fa["word"]
    for swear in swears:
        print(swear)
        assert sansor(swear) == str(len(swear) * "*")
