import re

years = input()
expression = r"\b(\d{2})+(\.|/|-)+([A-Z][a-z]+)+\2+(\d+)"
years_find = re.findall(expression, years)

for match in years_find:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
