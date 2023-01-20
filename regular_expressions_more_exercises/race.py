import re
text = input().split(", ")

pattern_name = r"[A-Z]|[a-z]"
pattern_km = r"\d"
distance_of_people = {}

line = input()
while line != "end of race":
    name = re.findall(pattern_name, line)
    name = "".join(name)
    if name in text:
        distance = re.findall(pattern_km, line)
        distance = [int(digit) for digit in distance]
        if distance:
            if name not in distance_of_people:
                distance_of_people[name] = sum(distance)
            else:
                distance_of_people[name] += sum(distance)
    line = input()

statistics = sorted(distance_of_people.items(), key=lambda item: item[1], reverse=True)
first_three = statistics[0:3]
winners = [winner[0] for winner in first_three]

place = 0
for winner in winners:
    place += 1
    if place == 1:
        print(f"1st place: {winner}")
    elif place == 2:
        print(f"2nd place: {winner}")
    elif place == 3:
        print(f"3rd place: {winner}")
