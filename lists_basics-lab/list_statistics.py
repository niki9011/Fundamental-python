number_line = int(input())

positive = []
negative = []

for num in range(number_line):
    current_num = int(input())
    if current_num >= 0:
        positive.append(current_num)
    else:
        negative.append(current_num)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
