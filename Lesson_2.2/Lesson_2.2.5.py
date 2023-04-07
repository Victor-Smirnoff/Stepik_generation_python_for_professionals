def get_sum_of_numbers(number):
    count = 0
    while number > 0:
        num = number % 10
        count += num
        number //= 10
    return count


n = int(input())

lst = list(range(1, n + 1))

tmp = [get_sum_of_numbers(x) for x in lst]

d = {}

for i in range(min(tmp), max(tmp) + 1):
    d[i] = []
    for x in lst:
        if get_sum_of_numbers(x) == i:
            d[i].append(x)

print(len(max(d.values(), key=len)))
