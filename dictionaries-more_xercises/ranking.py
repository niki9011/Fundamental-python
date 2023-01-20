contests = {}
submissions = {}
group_ranking = []

while True:
    input_line = input()
    if input_line == 'end of contests':
        break

    contest, password = input_line.split(':')
    contests[contest] = password

while True:
    input_line = input()
    if input_line == 'end of submissions':
        break

    contest, password, user, pts = input_line.split('=>')

    if contest in contests and contests.get(contest) == password:
        
        if user in submissions and contest in submissions.get(user):
            current_points = submissions[user][contest]
            submissions[user][contest] = max(current_points, int(pts))

        elif user in submissions:
            submissions[user][contest] = int(pts)

        else:
            submissions[user] = {contest: int(pts)}

for user in submissions.keys():
    total_pts = sum(submissions[user].values())
    group_ranking.append((user, total_pts))

sorted_ranking = sorted(group_ranking, key=lambda item: -item[1])
print(f"Best candidate is {sorted_ranking[0][0]} with total {sorted_ranking[0][1]} points.")

sorted_users = sorted([user for user in submissions.keys()])

print('Ranking:')
for user in sorted_users:
    user_submissions = [u_s for u_s in sorted(submissions[user].items(), key=lambda item: -item[1])]
    output = [f'#  {contest} -> {points}' for (contest, points) in user_submissions]
    print(user)
    print(*output, sep='\n')

