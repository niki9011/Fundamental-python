from math import  floor
number_group = int(input())
days = int(input())
companions_count = 0
coins = 0
for i in range(1, days + 1):
    coins += 50
    if i % 10 == 0:
        number_group -= 2
    if i % 15 == 0:
        number_group += 5
    if i % 3 == 0:
        coins -= number_group * 3
    if i % 5 == 0:
        coins += number_group * 20
        if i % 3 == 0:
            coins -= number_group * 2
    coins -= number_group * 2
print(f"{number_group} companions received {floor(coins / number_group)} coins each.")



