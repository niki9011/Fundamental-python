number_days = int(input())
number_players = int(input())
group_energy = float(input())
water_person_day = float(input())
food_person_day = float(input())
flag = False

total_water = number_days * number_players * water_person_day
total_food = number_days * number_players * food_person_day

for day in range(1, number_days + 1):
    if group_energy <= 0:
        flag = True
        break
    energy_loss = float(input())

    group_energy -= energy_loss
    if group_energy <= 0:
        flag = True
        break

    if day % 2 == 0:
        group_energy = group_energy + (group_energy * 0.05)
        total_water = total_water - (total_water * 0.30)
        if group_energy <= 0:
            flag = True
            break

    if day % 3 == 0:
        total_food = total_food - (total_food / number_players)
        group_energy = group_energy + (group_energy * 0.10)
        if group_energy <= 0:
            flag = True
            break

    if group_energy <= 0:
        flag = True
        break

if flag:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
