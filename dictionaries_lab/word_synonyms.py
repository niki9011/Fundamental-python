number = int(input())
synonyms = dict()

for num in range(number):

    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = [synonym]

    else:
        synonyms[word].append(synonym)
for s in synonyms:
    value = ", ".join(synonyms[s])
    print(f"{s} - {value}")
