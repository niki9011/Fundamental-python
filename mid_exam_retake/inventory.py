items = input().split(", ")

while True:
    command = input()

    if command == "Craft!":
        break

    else:
        command = command.split(" - ")
        if command[0] == "Collect":
            if command[1] not in items:
                items.append(command[1])
            else:
                continue

        if command[0] == "Drop":
            if command[1] in items:
                items.pop(items.index(command[1]))
            else:
                continue

        elif command[0] == "Combine Items":
            old_item, new_item = command[1].split(":")
            if old_item in items:

                items.insert(items.index(old_item) + 1, new_item)
            else:
                continue

        elif command[0] == "Renew":
            if command[1] in items:
                items.pop(items.index(command[1]))
                items.append(command[1])

print(", ".join(items))
