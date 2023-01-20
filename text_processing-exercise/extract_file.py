text = input().split('\\')
data = []

data.append(text[-1])
file_name = "".join(data).split('.')

print(f"File name: {file_name[0]}")
print(f"File extension: {file_name[1]}")

