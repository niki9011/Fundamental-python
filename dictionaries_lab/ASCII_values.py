characters = input().split(", ")

result = {}

for char in characters:
    result[char] = ord(char)
print(result)
