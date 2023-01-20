import re

text = input()
result = []
word_result = []
word_found = []

pattern = r'[@][A-Za-z]{3,}[@][@][A-Za-z]{3,}[@]|[#][A-Za-z]{3,}[#][#][A-Za-z]{3,}[#]'
pattern_new = r"([a-zA-Z]+)"

search_word = re.finditer(pattern, text)

for n in search_word:
    result.append(n.group())

for i in result:
    word = re.finditer(pattern_new, i)
    for x in word:
        word_result.append(x.group())
    if word_result[0] == word_result[1][::-1]:
        word_found.append(f"{word_result[0]} <=> {word_result[1]}")
        word_result.clear()
    else:
        word_result.clear()
        continue

if word_found:
    print(f"{len(result)} word pairs found!")
    print(f"The mirror words are:")
    print(", ".join(word_found))

else:
    if result:
        print(f"{len(result)} word pairs found!")
        print(f"No mirror words!")
    else:
        print("No word pairs found!")
        print("No mirror words!")
