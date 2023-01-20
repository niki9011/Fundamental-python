start = input()
end = input()
name = input()

data = 0
characters = []
range_char = []

for x in name:
    characters.append(x)

for n in range(ord(start) + 1, ord(end)):
    range_char.append(chr(n))

for char in characters:
    if char in range_char:
        data += ord(char)

print(data)
