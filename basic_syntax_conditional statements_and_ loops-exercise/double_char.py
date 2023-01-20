string = ''

while True:
    command = input()
    if command == "End":
        break

    elif command == "SoftUni":
        continue

    else:
        for i in command:
            string += i * 2
        print(string)
        string = ''

    text = input()
