number_cars = int(input())
cars_collections = {}
recharge = 0

for num in range(number_cars):
    car_info = input().split("|")

    car = car_info[0]
    mileage = int(car_info[1])
    fuel = int(car_info[2])

    cars_collections[car] = [mileage, fuel]

while True:

    command = input().split(" : ")

    if command[0] == "Stop":
        break

    elif command[0] == "Drive":
        car_info = command[1]
        distance = int(command[2])
        fuel_info = int(command[3])

        if cars_collections[car_info][1] > fuel_info:
            cars_collections[car_info][0] += distance
            cars_collections[car_info][1] -= fuel_info
            print(f"{car_info} driven for {distance} kilometers. {fuel_info} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")

        if cars_collections[car_info][0] > 100000:
            print(f"Time to sell the {car_info}!")
            del cars_collections[car_info]

    elif command[0] == "Refuel":
        car_name = command[1]
        fuel_recharge = int(command[2])

        if cars_collections[car_name][1] + fuel_recharge < 75:
            cars_collections[car_name][1] += fuel_recharge
            print(f"{car_name} refueled with {fuel_recharge} liters")
        else:
            recharge = 75 - cars_collections[car_name][1]
            cars_collections[car_name][1] += recharge
            print(f"{car_name} refueled with {recharge} liters")

    elif command[0] == "Revert":
        car_reset = command[1]
        amount_reverted = int(command[2])

        cars_collections[car_reset][0] -= amount_reverted
        if cars_collections[car_reset][0] < 10000:
            cars_collections[car_reset][0] = 10000
        else:
            print(f"{car_reset} mileage decreased by {amount_reverted} kilometers")

for key, value in cars_collections.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")
