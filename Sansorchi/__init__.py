from json import loads

file = open("/usr/lib/python3.8/sansorchi/data.json", "r")
Json = loads(file.read())["word"]


def sansor(txt: str, bad=Json, **kwargs) -> str:
    """ This function takes an obligatory input called
    >>> txt and deletes it if there is an insult in it."""
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
