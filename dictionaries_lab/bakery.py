some_products = input().split()
bakery = {}

for product in range(0, len(some_products), 2):
    key = some_products[product]
    value = some_products[product + 1]
    bakery[key] = int(value)

print(bakery)
