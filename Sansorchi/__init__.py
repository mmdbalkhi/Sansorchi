from .data import Json

Json = Json["word"]


def sansor(txt: str, bad=Json, **kwargs) -> str:
    """ This function takes an obligatory input called
    >>> txt and deletes it if there is an insult in it."""
    split = txt.split(
        " ")  # BUG: This creates bug line, Separate words from space.
    # >>>>>>>>> Multi-part words are separated
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
