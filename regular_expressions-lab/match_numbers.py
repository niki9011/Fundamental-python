import re

numbers = input()

match_numbers = re.finditer(r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))", numbers)

output = []

for match in match_numbers:
    output.append(match.group())
print(' '.join(output))
