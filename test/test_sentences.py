"""Testing Sansorchi package"""

from sansorchi import __version__, data, sansor

txts = ["تو موزی موز", "خنگ خدا", "خر به پیش", "حیوانی وحشی"]
outputs = [" تو ***ی ***", "*** خدا ", "*** به پیش ", "***** وحشی "]


def test_sentences():
    """Test with up Lists"""
    i = 0
    for txt in txts:
        i += 1
        assert sansor(txt) == outputs[i - 1]


def test_version():
    assert __version__ == "4.0"


print(__version__)
