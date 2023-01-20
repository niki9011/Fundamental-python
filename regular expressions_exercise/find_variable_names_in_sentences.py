import re

text = input()

result = []

numbers = re.findall(r"\b_[a-zA-Z0-9]+\b", text)

for word in numbers:
    result.append(word[1:])

print(",".join(result))