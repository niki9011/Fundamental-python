dragons = {}
dtypes = []
default_stats = (45, 250, 10)

for _ in range(int(input())):
	dtype, name, dmg, hp, ac = input().split(' ')
	dmg, hp, ac = (default_stats[i] if x == 'null' else int(x) for i, x in enumerate((dmg, hp, ac)))
	
	key = (dtype, name)
	value = (dmg, hp, ac)
	dragons[key] = value
	
	if dtype not in dtypes:
		dtypes.append(dtype)
	
for dtype in dtypes:
	stats = [v for k, v in dragons.items() if k[0] == dtype]
	dmg, hp, ac = [sum(item) / len(item) for item in zip(*stats)]
	print(f'{dtype}::({dmg:.2f}/{hp:.2f}/{ac:.2f})')
	
	filtered_dragons = {k[1]: v for k, v in dragons.items() if k[0] == dtype}
	output = {k: v for k, v in sorted(filtered_dragons.items(), key=lambda item: item[0])}
	for k, v in output.items():
		print(f'-{k} -> damage: {v[0]}, health: {v[1]}, armor: {v[2]}')
