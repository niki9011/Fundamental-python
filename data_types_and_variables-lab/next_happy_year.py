years = int(input())

happy_years = False

while not happy_years:
    years += 1
    str_years = str(years)
    set_years = set(str_years)
    happy_years = len(str_years) == len(set_years)

print(years)