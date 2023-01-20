tier = {}

while True:
	input_line = input()
	if input_line == 'Season end':
		break
	
	if ' -> ' in input_line:
		player, possition, skill = input_line.split(' -> ')
		
		if player not in tier:
			tier[player] = {possition: int(skill)}
			
		elif possition not in tier[player].keys():
			tier[player][possition] = int(skill)
		
		else:
			tier[player][possition] = max(tier[player][possition], int(skill))
		
	elif ' vs ' in input_line:
		p1, p2 = input_line.split(' vs ')
		
		if p1 in tier.keys() and p2 in tier.keys():	
			for p1_position in tier[p1].keys():
				if p1_position in tier[p2].keys():
					p1_skill = sum(tier[p1].values())
					p2_skill = sum(tier[p2].values())
					if p1_skill < p2_skill:
						tier.pop(p1)
					elif p2_skill < p1_skill:
						tier.pop(p2)
					break

player_pts = [(p, sum(tier[p].values())) for p in tier.keys()]
player_ranking = [rank for rank in sorted(player_pts, key= lambda item: (-item[1], item[0]))]

for rank in player_ranking:
    player, skill = rank
    print(f"{player}: {skill} skill")
    position_ranking = [rank for rank in sorted(tier[player].items(), key= lambda item: (-item[1], item[0]))]
    output = [f'- {pos} <::> {skill}' for pos, skill in position_ranking]
    print(*output, sep='\n')
