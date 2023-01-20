numbers = sorted(list(map(int, input().split(' '))), reverse=True)
top_5 = [n for n in numbers if n > (sum(numbers) / len(numbers))][:5]
print('No' if len(top_5) == 0 else ' '.join(map(str, top_5)))


