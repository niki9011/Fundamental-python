nums = input().split()
command = input().split()

data = []
counter = 0
len_nums = len(nums)

while True:

    if command[0] == "end":
        break

    elif command[0] == "swap":
        nums[int(command[1])], nums[int(command[2])] = nums[int(command[2])], nums[int(command[1])]

    elif command[0] == "multiply":
        nums[int(command[1])] = int(nums[int(command[1])]) * int(nums[int(command[2])])
        for num in range(len(nums)):
            nums[num] = str(nums[num])

    elif command[0] == "decrease":
        data = nums.copy()
        nums.clear()
        for x in data:
            nums.append(int(x) - 1)
        for i in range(len(nums)):
            nums[i] = str(nums[i])

    command = input().split()

print(", ".join(nums))
