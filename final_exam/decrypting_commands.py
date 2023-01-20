text = input()

while True:
    command = input().split()
    if command[0] == "Finish":
        break

    elif command[0] == "Replace":
        current_char = command[1]
        new_char = command[2]
        text = text.replace(current_char, new_char)
        print(text)

    elif command[0] == "Cut":
        star_index = int(command[1])
        end_index = int(command[2])
        if 0 <= star_index <= end_index < len(text):
            text = text[:star_index] + text[end_index + 1:]
            print(text)
        else:
            print("Invalid indices!")

    elif command[0] == "Make":
        if command[1] == "Upper":
            text = text.upper()
            print(text)
        elif command[1] == "Lower":
            text = text.lower()
            print(text)

    elif command[0] == "Check":
        string = command[1]
        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif command[0] == "Sum":
        index_start = int(command[1])
        index_end = int(command[2])
        suma_chars = 0
        if 0 <= index_start <= index_end < len(text):
            char_index = text[index_start:index_end + 1]
            for char in char_index:
                suma_chars += ord(char)
            print(suma_chars)
        else:
            print("Invalid indices!")

# string = input()
#
# while True:
#     command = input().split()
#
#     if command[0] == "Finish":
#         break
#
#     elif command[0] == "Replace":
#         current_char = command[1]
#         new_char = command[2]
#         if current_char in string:
#             string = string.replace(current_char, new_char)
#             print(string)
#
#     elif command[0] == "Cut":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         if 0 <= start_index <= end_index < len(string):
#             string = string[:start_index] + string[end_index + 1:]
#             print(string)
#         else:
#             print("Invalid indices!")
#
#     elif command[0] == "Make":
#         upper_or_lower = command[1]
#         if upper_or_lower == "Upper":
#             string = string.upper()
#             print(string)
#         else:
#             string = string.lower()
#             print(string)
#
#     elif command[0] == "Check":
#         character = command[1]
#         if character in string:
#             print(f"Message contains {character}")
#         else:
#             print(f"Message doesn't contain {character}")
#
#     elif command[0] == "Sum":
#         start_index = int(command[1])
#         end_index = int(command[2])
#         char_sum = 0
#         if 0 <= start_index <= end_index < len(string):
#             for num in range(start_index, end_index + 1):
#                 char_sum += ord(string[num])
#             print(char_sum)
#         else:
#             print("Invalid indices!")
