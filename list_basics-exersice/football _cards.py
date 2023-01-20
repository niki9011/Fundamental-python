cards = input().split(" ")

team_A = [1] * 11
team_B = [1] * 11
flag = False

for card in cards:

    tokens = card.split("-")
    team = tokens[0]
    player = int(tokens[1])
    idx = player - 1

    if team == "A":
        team_A[idx] = 0
        if team_A[idx] == 0:
            if sum(team_A) < 7 or sum(team_B) < 7:
                flag = True
                break
            continue

    if team == "B":
        team_B[idx] = 0
        if team_A[idx] == 0:
            if sum(team_A) < 7 or sum(team_B) < 7:
                flag = True
                break
            continue

print(f"Team A - {sum(team_A)}; Team B - {sum(team_B)}")
if flag:
    print("Game was terminated")
