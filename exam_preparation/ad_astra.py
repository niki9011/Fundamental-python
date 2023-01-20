import re

destination = input()

regex = r"([=/])([A-Z][A-Za-z]{2,})\1"

find_destination = re.finditer(regex, destination)
points = 0
list_destinations = []

for find in find_destination:
    city = find[2]
    list_destinations.append(city)
    points += len(city)

output = ", ".join(list_destinations)
print(f"Destinations: {output}")
print(f"Travel Points: {points}")
