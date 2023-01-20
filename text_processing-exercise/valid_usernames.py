import string

def valid_usernames(word):
    element = string.digits + string.ascii_letters+ "-" + "_"
    data = []

    for word in username:
        if 3 <= len(word) <= 16:
            data = [char for char in word if char in element]

            if len(word) == len(data):
                print("".join(data))

username = input().split(', ')
valid_usernames(username)

