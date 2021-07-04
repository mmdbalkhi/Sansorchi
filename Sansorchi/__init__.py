from .data import Json

Json = Json["fa"]


def sansor(txt: str, bad=Json, lang="fa", **kwargs) -> str:
    """ This function takes an obligatory input called
    txt and deletes it if there is an insult in it
    >>> sansor('موز خر است') == "م**ز خ**ر است' # Farsi
    """

    if lang == "fa":
        txt = txt.replace("‌", "")
    
    split = txt.split(" ")

    a = ''
    for i in split:
        if i in bad:
            badi = str(i[0]) + "**" + str(i[-1])
            a += badi
        else:
            a += i
        if split[-1] != i:
            a += " "
    return a
