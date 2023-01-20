price_ratings = list(map(int, input().split(", ")))
entry_point = int(input())
type_items = input()

left_damage = 0
right_damage = 0
value_entry_point = price_ratings[entry_point]
left_items = price_ratings[:entry_point]
right_items = price_ratings[entry_point + 1:]
position = ""

if type_items == "cheap":
    for num_left in left_items:
        if num_left < value_entry_point:
            left_damage += num_left

    for num_right in right_items:
        if num_right < value_entry_point:
            right_damage += num_right

elif type_items == "expensive":
    for left_num in left_items:
        if left_num >= value_entry_point:
            left_damage += left_num

    for right_num in right_items:
        if right_num >= value_entry_point:
            right_damage += right_num

if right_damage > left_damage:
    position = "Right"
    print(f"{position} - {right_damage}")
else:
    position = "Left"
    print(f"{position} - {left_damage}")
