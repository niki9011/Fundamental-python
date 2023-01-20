import string

text = input()

emoticon = ""
flag = False

for char in text:
    if flag:
        emoticon += char
        print(emoticon)
        emoticon = ""
        flag = False

    if char == ":":
        emoticon += char
        flag = True
