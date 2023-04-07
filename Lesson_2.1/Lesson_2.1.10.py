def choose_plural(amount, declensions):
    if amount % 10 in (2, 3, 4) and amount % 100 not in range(12, 15):
        return str(amount) + ' ' + str(declensions[1])
    if amount % 10 in (5, 6, 7, 8, 9, 0) or amount % 100 in range(10, 21):
        return str(amount) + ' ' + str(declensions[2])
    if amount % 100 != 11 and amount % 10 == 1:
        return str(amount) + ' ' + str(declensions[0])
