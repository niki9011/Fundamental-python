n = int(input())

for i in range(n):
    numbers = int(input())

    if numbers % 2 == 1:
        print(f"{numbers} is odd!")
        break
else:
    print("All numbers are even.")