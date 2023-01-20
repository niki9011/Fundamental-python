encrypted_data = input()

numbers = []
non_nums = []

for s in encrypted_data:
    if s.isdigit():
        numbers.append(int(s))
    else:
        non_nums.append(s)
        
take_list = [n for i, n in enumerate(numbers) if i % 2 == 0]
skip_list = [n for i, n in enumerate(numbers) if i % 2 != 0]

result = []
take_idx = 0
skip_idx = 0
start_idx = 0
round = 0

while True:
    if round == len(take_list):
        break
    round += 1
    
    for take in range(start_idx, (start_idx+take_list[take_idx])):
        if take == len(non_nums):
            break
            
        result.append(non_nums[take])
    start_idx += take_list[take_idx]
    start_idx += skip_list[skip_idx]
    take_idx += 1
    skip_idx += 1
    
print(f'{"".join(result)}')
