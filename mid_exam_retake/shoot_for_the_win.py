def reduce_values(targets_sequence, index):
    special_value = targets_sequence[index]
    targets_sequence[index] = -1

    for x in range(len(targets_sequence)):
        if targets_sequence[x] == -1:
            continue
        else:
            if targets_sequence[x] > special_value:
                targets_sequence[x] -= special_value
            else:
                targets_sequence[x] += special_value
    return targets_sequence


def shoot_func(targets_sequence):
    count_shoot = 0

    while True:
        command = input()

        if command == "End":
            break

        index = int(command)

        if 0 <= index < len(targets_sequence) and targets_sequence[index] != -1:
            count_shoot += 1
            reduce_values(targets_sequence, index)
    convert_target_to_string = [str(num) for num in targets_sequence]
    print(f"Shot targets: {count_shoot} ->  {' '.join(convert_target_to_string)}")

data = list(map(int, input().split()))
shoot_func(data)
