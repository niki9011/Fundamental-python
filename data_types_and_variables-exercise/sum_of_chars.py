number_characters = int(input())

result = 0

for char in range(number_characters):
    char = input()
    result += ord(char)

print(f"The sum equals: {result}")
