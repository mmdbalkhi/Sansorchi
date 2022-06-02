from sansorchi import Sansorchi

sansorchi = Sansorchi(level=None)


def test_repr():
    assert str(sansorchi) == "Sansorchi(None)"


def test_not_is_bad():
    assert not sansorchi.is_bad_word("سلام")
