numbers = input().split(" ")

invert_value = []

for num in numbers:
    if int(num) > 0:
        invert_value.append(-int(num))
    else:
        invert_value.append(abs(int(num)))

print(invert_value)
