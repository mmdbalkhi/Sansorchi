"""Testing Sansorchi package"""
import pytest

from sansorchi import Sansorchi

sansorchi = Sansorchi(level=None)

txts = ["خر حیوانی نجیب است", "خر یک گوسفند خورد"]
outputs = [" حیو نجیب است", " یک  خورد"]


@pytest.mark.parametrize("txt, output", zip(txts, outputs))
def test_text(txt, output):
    assert sansorchi.remove_bad_words(txt) == output
