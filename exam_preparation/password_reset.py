password = input()
data = input()
name = ""

while data != "Done":
    command = data.split()

    if command[0] == "TakeOdd":
        for char in range(len(password)):
            if char % 2 != 0:
                name += password[char]
        password = name
        name = ""
        print(password)


    elif command[0] == "Cut":
        index_start = int(command[1])
        index_finish = int(command[1]) + int(command[2])
        password = password[:index_start] + password[index_finish:]
        print(password)


    elif command[0] == "Substitute":
        if command[1] in password:
            old = command[1]
            new = command[2]
            password = password.replace(old, new)
            print(password)
        else:
            print("Nothing to replace!")

    data = input()

print(f"Your password is: {password}")
