from Sansorchi import sansor, data

txts = ["تو موزی موز", "خنگ خدا", "خر به پیش", "حیوانی وحشی"]
outputs = ["تو موزی م**ز", "خ**گ خدا", "خ**ر به پیش", "ح**ی وحشی"]


def test_sentences():
    i = 0
    for txt in txts:
        i += 1
        assert sansor(txt) == outputs[i - 1]


def test_word():
    words = data.fa["word"]
    for word in words:

        assert sansor(word) == word[0] + "**" + word[-1]
