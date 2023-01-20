string = input().split(" ")
data = ""

for word in string:
   data += word * len(word)

print(data)
