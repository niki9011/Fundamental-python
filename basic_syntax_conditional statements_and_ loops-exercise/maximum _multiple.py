n1 = int(input())
n2 = int(input())
max_num = []

for num in range(n2, 0, -1):
    if num % n1 == 0:
        max_num.append(num)

print(max_num[0])

