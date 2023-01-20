factor_number = int(input())
count_number = int(input())

list_count = []

for num in range(1, count_number + 1):
    list_count.append(num * factor_number)

print(list_count)
