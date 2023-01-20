def calculations(operator_command, num_one, num_two):
    if operator_command == "subtract":
        return int(num_one - num_two)
    elif operator_command == "divide":
        return int(num_one / num_two)
    elif operator_command == "add":
        return int(num_one + num_two)
    elif operator_command == "multiply":
        return int(num_one * num_two)


operator = input()
number_one = int(input())
number_two = int(input())
print(calculations(operator, number_one, number_two))