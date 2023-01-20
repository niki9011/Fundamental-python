budget = int(input())
command = input()

while True:

    if command == "End":
        print("You bought everything needed.")
        break
    budget -= int(command)

    if budget < 0:
        print("You went in overdraft!")
        break

    command = input()