numbers = list(map(int, input().split(', ')))

nums_list, zero_list = [], []

for num in numbers:
    if num != 0:
        nums_list.append(num)
    else:
        zero_list.append(num)

print(nums_list + zero_list)
