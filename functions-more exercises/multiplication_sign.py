def multiplication_sign():
    num_list = []
    for _ in range(3):
        num_list.append(int(input()))

    count_negative = len(list(filter(lambda x: x < 0, num_list)))
    count_zeroes = len(list(filter(lambda x: x == 0, num_list)))

    if count_zeroes > 0:
        return 'zero'
    elif count_negative == 1 or count_negative == 3:
        return 'negative'
    else:
        return 'positive'


print(multiplication_sign())
