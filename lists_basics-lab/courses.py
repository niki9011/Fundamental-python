numbers = int(input())

count_positives = list()
sum_of_negatives = list()

for n in range(numbers):
    num = int(input())
    if num >= 0:
        count_positives.append(num)
    else:
        sum_of_negatives.append(num)

print(count_positives)
print(sum_of_negatives)
print(f"Count of positives: {len(count_positives)}")
print(f"Sum of negatives: {sum(sum_of_negatives)}")
