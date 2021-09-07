"""Testing Sansorchi package"""

from sansorchi import sansor

txts = ["تو موزی موز", "خنگ خدا", "خر به پیش", "حیوانی وحشی"]
outputs = ["تو ***ی *** ", "*** خدا ", "** به پیش ", "*****ی وحشی "]


def test_sentences():
    """Test with up Lists"""
    i = 0
    for txt in txts:
        i += 1
        assert sansor(txt) == outputs[i - 1]
