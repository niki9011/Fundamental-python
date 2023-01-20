words = input().split()
data = {}

for word in words:
    word = word.lower()
    if word not in data:
        data[word] = 0

    data[word] += 1

for key, value in data.items():
    if value % 2 != 0:
        print(key, end=" ")
