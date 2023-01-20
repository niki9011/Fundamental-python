key, n = int(input()), int(input())

messege = ''

for char in range(n):
    character = input()
    ascii_number = ord(character) + key
    messege += chr(ascii_number)

print(messege)