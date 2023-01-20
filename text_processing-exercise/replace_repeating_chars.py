text = input()

result = ""
data = ""

for char in text:
    if char != data:
        result += char
        data = char

print(result)
