numbers = input()
string = input()

message = []
list_numbers = []
list_string = []
index = 0
result = 0

for char in string:
    list_string.append(char)

for num in numbers:
    list_numbers.append(num)

for i in list_numbers:

    if i != ' ':
        index += int(i)

    elif i == " ":
        if index > len(list_string):
            result = index - len(list_string)
            message.append(list_string[result])
            list_string.pop(result)
            index = 0

        else:
            message.append(list_string[index])
            list_string.pop(result)
            index = 0

if index > len(list_string):
    result = index - len(list_string)
    message.append(list_string[result])

else:
    message.append(list_string[index])

print(''.join(message))
