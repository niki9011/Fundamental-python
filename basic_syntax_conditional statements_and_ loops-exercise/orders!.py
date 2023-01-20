orders = int(input())

price = 0
total = 0

for i in range(orders):
    price_capsule = float(input())
    days = int(input())
    capsule_day = int(input())

    if 0.01 > price_capsule or price_capsule > 100:
        continue

    elif 0 >= days or days > 31:
        continue

    elif 1 > capsule_day or capsule_day > 2000:
        continue

    else:
        price = (price_capsule * capsule_day) * days
        total += price

    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total:.2f}")
