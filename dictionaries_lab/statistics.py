product = input()
statistics = {}

while product != "statistics":
    command = product.split()
    key = command[0]
    value = command[1]

    if key not in statistics:
        statistics[key] = int(value)
    else:
        statistics[key] = statistics.get(key) + int(value)

    product = input()

print("Products in stock:")

for num in statistics:
    print(f"- {num} {statistics[num]}")
print(f"Total Products: {len(statistics.keys())}")
print(f"Total Quantity: {sum(statistics.values())}")
