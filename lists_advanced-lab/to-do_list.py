data = []

while True:
    command = input().split('-')

    if command[0] == "End":
        break

    data.append((int(command[0]), command[1]))

sorted_data = [data_task[1] for data_task in sorted(data)]
print(sorted_data)
