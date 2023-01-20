coins = [int(num) for num in input().split(", ")]
number_beggars = int(input())

list_beggers = [0] * number_beggars
count = 0

for i in range(len(coins)):
    list_beggers[count] += coins[i]
    count += 1
    if count >= number_beggars:
        count = 0

print(list_beggers)
