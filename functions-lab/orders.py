def calculate_price(name_product, quantity_product ):
    if name_product == 'water':
        return quantity_product * 1.00

    elif name_product == 'coffee':
        return quantity_product * 1.50

    elif name_product == 'coke':
        return quantity_product * 1.40

    elif name_product == 'snacks':
        return quantity_product * 2.00

product = input()
quantity = float(input())

print(f"{calculate_price(product, quantity):.2f}")
