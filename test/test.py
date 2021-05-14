from Sansorchi import sansor, data

txts = ["تو موزی موز", "خنگ خدا", "خر به پیش", "حیوانی وحشی"]
outputs = ["تو موزی م**ز", "خ**گ خدا", "خ**ر به پیش", "ح**ی وحشی"]


def test_sentences():
    i = 0
    for txt in txts:
        i += 1
        assert sansor(txt) == outputs[i-1]


def test_word():
    words = data.Json["word"]
    for word in words:
        # TODO: Suport MultiPart words.The problem is from the split[init.py:9]
        if " " in word:
            continue
        assert sansor(word) == word[0]+"**"+word[-1]
