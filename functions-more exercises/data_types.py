def data_types(command, data):

    if command == "int":
        result = int(data) * 2
        return result

    elif command == "real":
        result = float(data) * 1.5
        return f"{result:.2f}"

    elif command == "string":
        return f"${data}$"


current_command = input()
data_type = input()
print(data_types(current_command, data_type))