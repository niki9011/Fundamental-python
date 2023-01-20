import re

number = int(input())

for num in range(number):
    text = input()

    name = re.findall(r"(?<=\@)[A-Za-z]+\b", text)
    search_name = "".join(name)

    age = re.findall(r"(?<=\#)[0-9]+\b", text)
    search_age = "".join(age)

    print(f"{search_name} is {search_age} years old.")

