hero_recruitment = {}


while True:
    command = input().split()

    if command[0] == "End":
        break

    elif command[0] == "Enroll":
        hero_name = command[1]
        if hero_name not in hero_recruitment:
            hero_recruitment[hero_name] = []
        else:
            print(f"{hero_name} is already enrolled.")

    elif command[0] == "Learn":
        name_hero = command[1]
        spell_name = command[2]
        if name_hero in hero_recruitment:
            if spell_name in hero_recruitment[name_hero]:
                print(f"{name_hero} has already learnt {spell_name}.")
            else:
                hero_recruitment[name_hero].append(spell_name)
        else:
            print(f"{name_hero} doesn't exist.")

    elif command[0] == "Unlearn":
        name_of_hero = command[1]
        spell_of_name = command[2]
        if name_of_hero in hero_recruitment:
            if spell_of_name in hero_recruitment[name_of_hero]:
                hero_recruitment[name_of_hero].remove(spell_of_name)
            else:
                print(f"{name_of_hero} doesn't know {spell_of_name}.")
        else:
            print(f"{name_of_hero} doesn't exist.")

print("Heroes:")

for name, spell in hero_recruitment.items():
    spells = ", ".join(spell)
    print(f"== {name}: {spells}")
