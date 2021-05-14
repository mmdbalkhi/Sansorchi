from Sansorchi import sansor

txts = ["تو موزی موز", "خنگ خدای موز"]
outputs = ["تو موزی م**ز", "خ**گ خدای م**ز"]


def test_answer():
    """Sansorchi library test"""
    i = 0
    for txt in txts:
        i += 1
        assert sansor(txt) == outputs[i-1]
