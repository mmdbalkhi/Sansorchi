"""Sansorchi a package for remove swears word"""
import re

from .data import fa

__all__ = ["sansor"]


def sansor(txt: str, bad_db=fa["word"]) -> str:
    """*** this func receives a text and processesit
    **** *and returns the processed text to the user
    *** *replaces swear words with length of that start Note: The
    ** word swear at any length Returns the length of that star
    >>> sansor('موز خر است') == "** ** است' # Farsi
    """

    txt = txt.replace("‌", "")

    split = txt.split(" ")
    return_txt = ""

    for text in split:
        swear_bool = False
        for swear in bad_db:
            if re.findall(swear, text):  # if swear word in text do this
                ret = re.sub(
                    swear, str(len(swear) * "*"), text
                )  # replace swear word with start
                return_txt += ret

                swear_bool = True
                break
        if not swear_bool:
            return_txt = return_txt + text

        if len(split) > 1:
            return_txt += " "

    return return_txt
