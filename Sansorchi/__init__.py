"""Sansorchi a pakage for remove swears word"""

from .data import fa

json_data = fa["word"]


def sansor(txt: str, bad=json_data, lang="fa", **kwargs) -> str:
    """This function takes an obligatory input called
    txt and deletes it if there is an insult in it
    >>> sansor('موز خر است') == "م**ز خ**ر است' # Farsi
    """

    if lang == "fa":
        txt = txt.replace("‌", "")

    split = txt.split(" ")

    return_txt = ""
    for i in split:
        if i in bad:
            badi = str(i[0]) + "**" + str(i[-1])
            return_txt += badi
        else:
            return_txt += i
        if split[-1] != i:
            return_txt += " "
    return return_txt
