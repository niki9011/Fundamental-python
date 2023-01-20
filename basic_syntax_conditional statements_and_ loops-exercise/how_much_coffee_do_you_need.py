text = input()
count = 0

while text != "END":

    if text == "coding" or text == "dog" or text == "cat" or text == "movie":
        count += 1
    elif text == "CODING" or text == "DOG" or text == "CAT" or text == "MOVIE":
        count += 2

    if text == "END":
        break

    text = input()

if count > 5:
    print("You need extra sleep")
else:
    print(count)