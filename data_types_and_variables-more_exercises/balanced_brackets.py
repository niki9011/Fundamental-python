n_line = int(input())
flag = False
data_simbols = []

for i in range(n_line):
    data = input()

    if '(' in data:
        data_simbols.append(data)
    elif ")" in data:
        data_simbols.append(data)
        if data_simbols[0] == "(":
            if data_simbols[1] == ")":
                flag = True
                data_simbols.clear()

if flag:
    print("BALANCED")
else:
    print("UNBALANCED")