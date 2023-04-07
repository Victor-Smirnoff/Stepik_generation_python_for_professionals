def get_first_num(num):
    while len(str(num)) > 1:
        num //= 10
    return num


def get_biggest(numbers):
    numbers = sorted(numbers, key=get_first_num, reverse=True)
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if int(str(numbers[j]) + str(numbers[j + 1])) < int(str(numbers[j + 1]) + str(numbers[j])):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    tmp = ''.join(map(str, numbers))
    return int(tmp) if numbers else -1
