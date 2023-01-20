items = input().split('|')
budget = int(input())

profit = 0
new_item_prices = []
data_prices = []
flag = False

for item in items:
    flag = False
    current_item_info = item.split('->')
    type_product = current_item_info[0]
    price = float(current_item_info[1])

    if type_product == "Clothes":
        if price <= 50:
            flag = True

    elif type_product == "Shoes":
        if price <= 35:
            flag = True

    elif type_product == "Accessories":
        if price <= 20.50:
            flag = True

    if flag:
        if budget >= price:
            budget -= price
            profit += price * 0.40
            new_price = price + (price * 0.40)
            new_item_prices.append(new_price)
            data_prices.append(f"{new_price:.2f}")

print(' '.join(data_prices))
print(f'Profit: {profit:.2f}')

total = budget + sum(new_item_prices)

if total >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
