name_list = input().split(", ")

sorted_list = sorted(name_list, key=lambda name: (-len(name), name))

print(sorted_list)