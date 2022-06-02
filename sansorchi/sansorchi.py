import re
from typing import Union

from hazm import Normalizer  # type: ignore

from .data import fa


class Sansorchi:
    """Remove Persian (Farsi) Swear Words

    :func:`remove_swear_words` removes Persian (Farsi) swear words from a given text.
    =====================================================================================
    :param text: text to remove swear words
    :type text: str
    :return: text without swear words
    """

    def __init__(self, level=None) -> None:
        self.level = level
        self.bad_words = fa["word"]

    def __repr__(self) -> str:
        return f"Sansorchi({self.level})"

    def remove_bad_words(self, text: Union[str, bytes], replace_text: str = "") -> str:
        if isinstance(text, bytes):  # pragma: no cover
            text = text.decode("utf-8")

        for word in self.bad_words:
            text = re.sub(word, replace_text, text)

        return text

    def is_bad_word(self, text: Union[str, bytes]) -> bool:
        for word in self.bad_words:
            if word in text:
                return True
        return False

    @staticmethod
    def normalize(text: Union[str, bytes]) -> str:  # pragma: no cover
        normalizer = Normalizer()
        return normalizer.normalize(text)
