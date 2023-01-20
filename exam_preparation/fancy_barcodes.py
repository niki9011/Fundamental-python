import re

numbers = int(input())

pattern_valid_email = r"@#{1,}[A-Z][a-zA-Z0-9]{4,}[A-Z]@#{1,}"

for num in range(numbers):
    email = input()
    flag = True

    valid = re.finditer(pattern_valid_email, email)

    for vali_email in valid:
        flag = False
        digit_email = re.findall("\d", vali_email.group())
        if digit_email:
            print(f'Product group: {"".join(digit_email)}')
        else:
            print("Product group: 00")

    if flag:
        print("Invalid barcode")
