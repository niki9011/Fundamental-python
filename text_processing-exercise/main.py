text = input()
text_list = []

for char in text:
    text_list.append(chr(ord(char) + 3))

print(''.join(text_list))