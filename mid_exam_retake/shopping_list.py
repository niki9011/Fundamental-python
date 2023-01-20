def urgent_func(shopping_data, name):
    if name not in shopping_data:
        shopping_data.insert(0, name)

    return shopping_data


def unnecessary_func(shopping_data, name):
    if name in shopping_data:
        shopping_data.pop(shopping_data.index(name))

    return shopping_data


def correct_func(shopping_data, name, new_name):
    if name in shopping_data:
        shopping_data.insert(shopping_data.index(name), new_name)
        shopping_data.pop(shopping_data.index(name))

    return shopping_data


def rearrange_func(shopping_data, name):
    if name in shopping_data:
        shopping_data.pop(shopping_data.index(name))
        shopping_data.append(name)

    return shopping_data


def shopping_list(shopping_data):
    while True:
        command_current = input().split()
        if len(command_current) == 2:
            command = command_current[0]
            name = command_current[1]
        else:
            command = command_current[0]
            name = command_current[1]
            new_name = command_current[2]


        if command == "Go":
            break
        elif command == "Urgent":
            urgent_func(shopping_data, name)

        elif command == "Unnecessary":
            unnecessary_func(shopping_data, name)

        elif command == "Correct":

            correct_func(shopping_data, name, new_name)

        elif command == "Rearrange":
            rearrange_func(shopping_data, name)

    print(", ".join(shopping_data))

data = input().split("!")
shopping_list(data)
