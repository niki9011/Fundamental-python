nums = input().split(' ')
copy_nums = list(map(int, nums))
count = int(input())

for _ in range(count):
    current_min = min(copy_nums)
    nums.remove(str(current_min))
    copy_nums.remove(current_min)

print(', ' .join(nums))
