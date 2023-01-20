command = input()

price_without_taxes = 0
taxes = 0
all_price = taxes + price_without_taxes

while True:

    if command == "special" or command == "regular":
        if command == "special":
            taxes += price_without_taxes * 0.20
            all_price = taxes + price_without_taxes
            all_price = all_price - (all_price * 0.10)
            break

        elif command == "regular":
            taxes += price_without_taxes * 0.20
            all_price += price_without_taxes + taxes
            break

    elif command != "special" or command != "regular":
        if float(command) > 0:
            price_without_taxes += float(command)
        else:
            print("Invalid price!")

    command = input()
if all_price > 0:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {all_price:.2f}$")
else:
    print("Invalid order!")
