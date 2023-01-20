def rounding(nums):
    round_list = []

    [num for num in nums if round_list.append(round(float(num)))]
    return round_list

numbers = input().split(" ")
print(rounding(numbers))
