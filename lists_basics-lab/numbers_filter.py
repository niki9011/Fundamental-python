numbers = int(input())

numbers_list = list()
result = list()
flag = False

while True:
    if flag:
        print(result)
        break
    command = input()

    if command == "even":
        for num in numbers_list:
            if num % 2 == 0:
                result.append(num)
                flag = True

    elif command == "odd":
        for num in numbers_list:
            if num % 2 != 0:
                result.append(num)
                flag = True

    elif command == "negative":
        for num in numbers_list:
            if num < 0:
                result.append(num)
                flag = True

    elif command == "positive":
        for num in numbers_list:
            if num >= 0:
                result.append(num)
                flag = True
    else:
        numbers_list.append(int(command))