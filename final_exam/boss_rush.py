import re

number = int(input())

for num in range(number):
    text = input()

    pattern = r"\|[A-Z]+\|\:#[A-Za-z]+\s[A-Za-z]+#"

    valid = re.findall(pattern, text)

    if valid:
        data = "".join(valid)
        boss = data.split("|")
        name = boss[1]
        simbol = data.split("#")
        title = simbol[1]
        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")

    else:
        print("Access denied!")

#
# numer = int(input())
# pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+ [A-Za-z]+)#"
#
# for x in range(numer):
#     flag = True
#     text = input()
#
#     find = re.finditer(pattern, text)
#
#     for n in find:
#         print(f"{n.group(1)}, The {n.group(2)}")
#         print(f">> Strength: {len(n.group(1))}")
#         print(f">> Armor: {len(n.group(2))}")
#         flag = False
#     if flag:
#         print("Access denied!")