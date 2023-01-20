small_letters = int(input())

for a in range(0, small_letters):
    for b in range(0, small_letters):
        for c in range(0, small_letters):
            print(f"{chr(a + 97)}{chr(b + 97)}{chr(c + 97)}")
