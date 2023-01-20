quantity_food_kg = float(input()) * 1000
quantity_hay_kg = float(input()) * 1000
cover_kg = float(input()) * 1000
weight_kg = float(input()) * 1000

for day in range(1, 31):
    quantity_food_kg -= 300

    if day % 2 == 0:
        quantity_hay_kg -= quantity_food_kg * 0.05
    if day % 3 == 0:
        cover_kg -= weight_kg / 3

if quantity_food_kg <= 0 or quantity_hay_kg <= 0 or cover_kg <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {(quantity_food_kg / 1000):.2f}, Hay: {(quantity_hay_kg / 1000):.2f}, Cover: {(cover_kg / 1000):.2f}.")


