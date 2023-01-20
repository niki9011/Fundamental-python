import re

output = []

while True:
    text = input()

    if not text:
        break

    numbers = re.findall(r"(\d+)", text)

    for match in numbers:
        output.append(match)

print(' '.join(output))



