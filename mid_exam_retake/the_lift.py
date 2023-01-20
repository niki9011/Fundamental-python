wait_people = int(input())
lift_numbers = list(map(int, input().split(' ')))

for lift in range(len(lift_numbers)):
    if wait_people > 3:
        numbers = 4 - lift_numbers[lift]
        wait_people -= numbers
        lift_numbers[lift] += numbers
    else:
        lift_numbers[lift] += wait_people
        wait_people = 0

if sum(lift_numbers) != len(lift_numbers) * 4:
    print("The lift has empty spots!")

elif wait_people > 0:
    print(f"There isn't enough space! {wait_people} people in a queue!")
print(" " .join([str(num) for num in lift_numbers]))
