name_coffees = input().split()
number = int(input())

for num in range(number):
    command = input().split()

    if command[0] == "Include":
        name_coffees.append(command[1])

    elif command[0] == "Remove":
        if command[1] == "first":
            [n for n in range(int(command[2])) if name_coffees.pop(0)]

        elif command[1] == "last":
            name_coffees.reverse()
            [n for n in range(int(command[2])) if name_coffees.pop(0)]
            name_coffees.reverse()

    elif command[0] == "Prefer":
        if int(command[1]) <= len(name_coffees) and int(command[2]) <= len(name_coffees):
            name_coffees[int(command[1])], name_coffees[int(command[2])] = name_coffees[int(command[2])], name_coffees[int(command[1])]
        else:
            continue

    elif command[0] == "Reverse":
        name_coffees.reverse()

print("Coffees:")
print(" ".join(name_coffees))
