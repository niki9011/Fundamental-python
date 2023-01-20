n = int(input())
flowers_dict = {}

for x in range(n):
    plant, rarity = input().split("<->")
    if plant not in flowers_dict:
        flowers_dict[plant] = [rarity, 0, 0]
    else:
        flowers_dict[plant] = [rarity, 0, 0]

while True:
    line = input().split()

    if line[0] == "Exhibition":
        break

    if line[1] in flowers_dict:
        if line[0] == "Rate:":
            if float(line[3]) > 0:
                name = line[1]
                rating = float(line[3])
                if name in flowers_dict:
                    flowers_dict[name][1] += rating
                    flowers_dict[name][2] += 1
            else:
                print("error")

        elif line[0] == "Update:":
            name = line[1]
            new_rarity = int(line[3])
            if name in flowers_dict:
                flowers_dict[name][0] = new_rarity

        elif line[0] == "Reset:":
            name = line[1]
            if name in flowers_dict:
                flowers_dict[name][1] = 0
    else:
        print("error")

print("Plants for the exhibition:")

for key, value in flowers_dict.items():
    rarity = flowers_dict[key][0]
    if flowers_dict[key][2] != 0:
        rating = float(flowers_dict[key][1]) / int(flowers_dict[key][2])
    elif flowers_dict[key][2] < 0:
        rating = 0.00
    else:
        rating = float(flowers_dict[key][1])

    print(f"- {key}; Rarity: {rarity}; Rating: {rating:.2f}")
