number = int(input())

hero_data = {}

for num in range(number):
    command = input().split()
    name, hp, mp = command[0], int(command[1]), int(command[2])
    hero_data[name] = [hp, mp]

while True:
    current_command = input()
    line = current_command.split(" - ")

    if line[0] == "End":
        break

    elif line[0] == "CastSpell":
        hero_name, mp_needed, spell_name = line[1], int(line[2]), line[3]
        if hero_data[hero_name][1] >= mp_needed:
            mp_remaining = hero_data[hero_name][1] - mp_needed
            hero_data[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {mp_remaining} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif line[0] == "TakeDamage":
        name_hero, damage, attacker = line[1], int(line[2]), line[3]
        hero_data[name_hero][0] -= damage
        if hero_data[name_hero][0] > 0:
            current_hp = hero_data[name_hero][0]
            print(f"{name_hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
        else:
            print(f"{name_hero} has been killed by {attacker}!")
            del hero_data[name_hero]

    elif line[0] == "Recharge":
        hero_of_name, amount = line[1], int(line[2])
        if hero_data[hero_of_name][1] + amount > 200:
            need_mp = 200 - hero_data[hero_of_name][1]
            hero_data[hero_of_name][1] = 200
            print(f"{hero_of_name} recharged for {need_mp} MP!")
        else:
            hero_data[hero_of_name][1] += amount
            print(f"{hero_of_name} recharged for {amount} MP!")

    elif line[0] == "Heal":
        name_of_hero, amount_hero = line[1], int(line[2])
        if hero_data[name_of_hero][0] + amount_hero > 100:
            amount_hp = 100 - hero_data[name_of_hero][0]
            hero_data[name_of_hero][0] = 100
            print(f"{name_of_hero} healed for {amount_hp} HP!")
        else:
            hero_data[name_of_hero][0] += amount_hero
            print(f"{name_of_hero} healed for {amount_hero} HP!")

for key, value in hero_data.items():
    print(key)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")
