numbers_string, word = int(input()), input()

string_all, word_filter = list(), list()

for string in range(numbers_string):
    current_string = input()
    string_all.append(current_string)
    if word in current_string:
        word_filter.append(current_string)

print(string_all), print(word_filter)
