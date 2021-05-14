from sansorchi import sansor

txts = ["تو موزی موز", "خنگ خدای موز"]
outputs = ["تو موزی م**ز", "خ**گ خدای م**ز"]

sucs = 0
i = 0
for txt in txts:
    i += 1
    if sansor(txt) == outputs[i-1]:
        sucs += 1
        print("\u001b[32m"+f"test {i}"+"\u001b[0m")
    else:
        print("\u001b[31m"+f"test {i}"+"\u001b[0m")

print(f"{sucs} test(s) is successfully")