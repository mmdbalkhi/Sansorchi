"""Testing Sansorchi package"""
import pytest

from sansorchi import data
from sansorchi import Sansorchi

sansorchi = Sansorchi(level=None)


@pytest.mark.parametrize("word", data.fa["word"])
def test_word(word):
    """Test word function"""
    assert sansorchi.remove_bad_words(word) == ""


@pytest.mark.parametrize("word", data.fa["word"])
def test_is_bad_word(word):
    """test is_bad_word function"""
    assert sansorchi.is_bad_word(text=word)
